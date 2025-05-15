# **Triton (~V3.2.0~ V3.3.0) Windows Native Build – NVIDIA Exclusive**
UPDATED to 3.3.0 
# ADDED 312 POWER!
~Note: this is for python 3.10(.6(?)), I was under the false impression i had labled it better, well, my bad. package says so but, i have no intention at this time unless there is actuall demand for other versions iee py311 or py312 etc. as ive not had a need want or reason to use those and so makes no sense to do so at this time for me until i either need it, or some large-scale use case demand is brought to my attention.~
Well that didn't take long, this repo is now/for-now Py310 and Py312!

# Check Releases for the latest most likely bug free version!
## Broken versions will be labeled

# UPDATE #
Found it broke for alot of others, if not all, but mine broke too thankfully and could track it down, after a VS update.
Found I had a custom file I used and didn't realize was part of the program working, you just need to add this to your MSVC's include folder, or any include path on your env that's active or always included.

so the short and sweet is add the CODE BLOCK as dlfcn.h to:

`"C:\ProgramFiles\MicrosoftVisualStudio\2022\Community\VC\Tools\MSVC\14.44.35207\include"`

As an exmple, you may have a different version/path/etc.
For anyone needing more... make a txt file, paste codeblock in text file, save, look at text file from outside and rename it to dlfcn.h DONE!

CODE BLOCK for dlfcn.h
```
//dlfcn.h

#ifndef WIN_DLFCN_H

#define WIN_DLFCN_H

#include <windows.h>

// Define POSIX-like handles

#define RTLD_LAZY 0

#define RTLD_NOW 0 // No real equivalent, Windows always resolves symbols

#define RTLD_LOCAL 0 // Windows handles this by default

#define RTLD_GLOBAL 0 // No direct equivalent

// Windows replacements for libdl functions

#define dlopen(path, mode) ((void*)LoadLibraryA(path))

#define dlsym(handle, symbol) (GetProcAddress((HMODULE)(handle), (symbol)))

#define dlclose(handle) (FreeLibrary((HMODULE)(handle)), 0)

#define dlerror() ("dlopen/dlsym/dlclose error handling not implemented")

#endif // WIN_DLFCN_H
```

---------------------------------------------------

### **🚀 Fully Native Windows Build (No VMs, No Linux Subsystems, No Workarounds)**
This is a **fully native** Triton build for **Windows + NVIDIA**, compiled **without any virtualized Linux environments** (no WSL, no Cygwin, no MinGW hacks). This version is built **entirely with MSVC**, ensuring **maximum compatibility, performance, and stability** for Windows users.  

🔥 **What Makes This Build Special?**  
- ✅ **100% Native Windows** (No WSL, No VM, No pseudo-Linux environments)  
- ✅ **Built with MSVC** (No GCC/Clang hacks, true Windows integration)  
- ✅ **NVIDIA-Exclusive** – **AMD has been completely stripped**  
- ✅ **Lightweight & Portable** – **Removed debug `.pdbs`, `.lnks`, and unnecessary files**  
- ✅ **Based on Triton's official LLVM build** (Windows blob repo)  
- ✅ **MSVC-CUDA Compatibility Tweaks** – NVIDIA’s **`driver.py`** and **runtime build** adjusted for Windows  
- ✅ **Runs on Windows 11 Insider Dev Build (RTX 3060, CUDA 12.1, Python 3.10.6)**  
- ✅ **Fully tested** – **Passed all standard tests, 86/120 focus tests (34 expected AMD-related failures)**  

---

## **🔧 Build & Technical Details**
- **Built for:** **Python 3.10.6 !NEW! && for: Python 3.12.10**  
- **Built on:** **Windows 11 Insiders Dev Build**  
- **Hardware:** **NVIDIA RTX 3060**  
- **Compiler:** **MSVC ([v14.43.34808] Microsoft Visual C++20)**  
- **CUDA Version:** **~12.1~ 12.8 (12.1 might work fine still if thats your installed kit version)**  
- **LLVM Source:** **Official Triton LLVM (Windows build, hidden in their blob repo)**  
- **Memory Allocation Tweaks:** **CUPTI modified to use `_aligned_malloc` instead of `aligned_alloc`**  
- **Optimized for Portability:** **No `.pdbs` or `.lnks` (Debuggers should build from source anyway)**  
- **Expected Warnings:** **Minimal "risky operation" warnings (e.g., pointer transfers, nothing major)**  
- **All Core Triton Components Confirmed Working:**  
  - **✅ Triton**  
  - **✅ libtriton**  
  - **✅ NVIDIA Backend**  
  - **✅ IR**  
  - **✅ LLVM**

## Flags Used

```
C/CXX Flags
--------------------------
/GL /GF /Gu /Oi /O2 /O1 /Gy- /Gw /Oi /Zo- /Ob1 /TP
/arch:AVX2 /favor:AMD64 /vlen
/openmp:llvm /await:strict /fpcvt:IA /volatile:iso
/permissive- /homeparams /jumptablerdata  
/Qspectre-jmp /Qspectre-load-cf /Qspectre-load /Qspectre /Qfast_transcendentals 
/fp:except /guard:cf
/DWIN32 /D_WINDOWS /DNDEBUG /D_DISABLE_STRING_ANNOTATION /D_DISABLE_VECTOR_ANNOTATION 
/utf-8 /nologo /showIncludes /bigobj 
/Zc:noexceptTypes,templateScope,gotoScope,lambda,preprocessor,inline,forScope
--------------------------
Extra(/Zc:):
C=__STDC__,__cplusplus-
CXX=__cplusplus-,__STDC__-
--------------------------
Link Flags:
/DEBUG:FASTLINK /OPT:ICF /OPT:REF /MACHINE:X64 /CLRSUPPORTLASTERROR:NO /INCREMENTAL:NO /LTCG /LARGEADDRESSAWARE /GUARD:CF /NOLOGO
--------------------------
Static Link Flags:
/LTCG /MACHINE:X64 /NOLOGO
--------------------------
CMAKE_BUILD_TYPE "Release"
```
  

---

### **🔥 Proton Active, AMD Stripped, NVIDIA-Only**
> This build retains **Proton as an active frontend** while **completely stripping AMD components** at every level, ensuring a **fully NVIDIA-native experience**.  
> - 🚀 **Proton is fully functional**, providing compatibility without AMD's HIP backend.  
> - ❌ **AMD's backend, dialects, and POSIX-specific implementations have been fully removed** to eliminate unnecessary dependencies and streamline performance.  
> - ✅ **Successfully builds and runs with NVIDIA components**, ensuring **CUDA support without fallback to AMD HIP.**  
> - ⚠️ **If your system uses "NVIDIA HIP" (rare case), it may not function correctly**, though this is an edge-case and not officially documented outside of Triton's source.  
> - 🔧 **This build is specifically optimized for CUDA-based NVIDIA GPUs and Windows environments.**  

🔥 **Proton remains intact, but AMD is fully stripped – a true NVIDIA + Windows Triton!** 🚀

---

## **🛠️ Compatibility & Limitations**
| Feature | Status |
|---------|--------|
| **CUDA Support** | ✅ Fully Supported (NVIDIA-Only) |
| **Windows Native Support** | ✅ Fully Supported (No WSL, No Linux Hacks) |
| **MSVC Compilation** | ✅ Fully Compatible |
| **AMD Support** | ❌ **Removed** (Stripped out at build level) |
| **POSIX Code Removal** | ✅ **Replaced with Windows-Compatible Equivalents** |
| **CUPTI Aligned Allocation** | ✅ May cause slight performance shift, but unconfirmed |

---

## **📜 Testing & Stability**
- **🏆 Passed all basic functional tests**
- **📌 Focus Tests: 86/120 Passed** (**34 AMD-specific failures, expected & irrelevant**)  
- **🛠️ No critical build errors** – only minor warnings related to transfers  
- **💨 xFormers tested successfully** – No Triton-related missing dependency errors  

---

## **📥 Download & Installation**
Install via pip:
```sh
Py312
pip install https://github.com/leomaxwell973/Triton-3.3.0-UPDATE_FROM_3.2.0_and_FIXED-Windows-Nvidia-Prebuilt/releases/download/3.3.0_cu128_Py312/triton-3.3.0-cp312-cp312-win_amd64.whl

Py310
pip install https://github.com/leomaxwell973/Triton-3.3.0-UPDATE_FROM_3.2.0_and_FIXED-Windows-Nvidia-Prebuilt/releases/download/3.3.0/triton-3.3.0-cp310-cp310-win_amd64.whl

```
Or from download:
```sh
pip install .\Triton-3.3.0-*-*-*-win_amd64.whl
```

---

## **💬 Final Notes**
This build is designed **specifically for Windows users with NVIDIA hardware**, eliminating unnecessary dependencies and optimizing performance. If you're developing **AI models on Windows and need a clean Triton setup without AMD bloat or Linux workarounds**, or have had difficulty building triton for Windows, this is **the best version available.**

## Also, I am aware of the "Windows" branch of Triton.
This version, last I checked, is for bypassing apps with a Linux/Unix/Posix focus platform, but have nothing that makes them strictly so, and thus, had triton as a no-worry requirement on a supported platform such as them, but no regard for windows, despite being compatible for them regardless. Or such case uses. It's a shell of triton, vaporware, that provides only token comparison of features or GPU enhancement compared to the full version of Linux. THIS REPO - Is such a full version, with LLVM and nothing taken out as long as its not involving AMD GPUs.

🔥 **Enjoy the cleanest, fastest Triton experience on Windows!** 🚀😎

If you'd like to show appreciation (donate) for this work: https://buymeacoffee.com/leomaxwell
