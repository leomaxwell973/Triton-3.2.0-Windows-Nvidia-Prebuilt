import sysconfig
import os
import shutil
import subprocess


def _build(name, src, srcdir, library_dirs, include_dirs, libraries):
    suffix = sysconfig.get_config_var('EXT_SUFFIX')
    so = os.path.join(srcdir, '{name}{suffix}'.format(name=name, suffix=suffix))

    # Try to find a C compiler
    cc = os.environ.get("CC")
    if cc is None:
        # Check for compilers: MSVC (cl.exe), Clang, GCC
        clang = shutil.which("clang")
        gcc = shutil.which("gcc")
        msvc = shutil.which("cl")
        if msvc is not None:
            cc = "cl"  # Use MSVC
        elif gcc is not None:
            cc = gcc
        elif clang is not None:
            cc = clang
        else:
            raise RuntimeError("Failed to find a C compiler. Please specify via CC environment variable.")

    # Get Python include directory
    if hasattr(sysconfig, 'get_default_scheme'):
        scheme = sysconfig.get_default_scheme()
    else:
        scheme = sysconfig._get_default_scheme()

    if scheme == 'posix_local':
        scheme = 'posix_prefix'

    py_include_dir = sysconfig.get_paths(scheme=scheme)["include"]
    custom_backend_dirs = set(os.getenv(var) for var in ('TRITON_CUDACRT_PATH', 'TRITON_CUDART_PATH'))
    include_dirs = include_dirs + [srcdir, py_include_dir, *custom_backend_dirs]

    # MSVC uses `/LD` instead of `-shared` and `/I` instead of `-I`
    if cc == "cl":
        so = so.replace("/", "\\")  # Convert path for Windows compatibility

        cc_cmd = [
            "cl", src, "/LD", "/O2", "/MD", "/Fe:" + so,
            *[f"/I{dir}" for dir in include_dirs if dir is not None],  # Include dirs
            *[f"/link"],
            *[f"/LIBPATH:{dir}" for dir in library_dirs]  # Library paths
        ]
        cc_cmd += [f"{lib}.lib" for lib in libraries]  # Link static libraries

    else:  # GCC/Clang (original logic)
        cc_cmd = [cc, src, "-O3", "-shared", "-fPIC", "-Wno-psabi", "-o", so]
        cc_cmd += [f'-l{lib}' for lib in libraries]
        cc_cmd += [f"-L{dir}" for dir in library_dirs]
        cc_cmd += [f"-I{dir}" for dir in include_dirs if dir is not None]

    subprocess.check_call(cc_cmd, stdout=subprocess.DEVNULL)
    return so
