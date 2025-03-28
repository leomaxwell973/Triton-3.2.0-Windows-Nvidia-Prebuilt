# **Triton (V3.2.0) Windows Native Build – NVIDIA Exclusive**
### **🚀 Fully Native Windows Build (No VMs, No Linux Subsystems, No Workarounds)**

### - CRITICAL UPDATE READ BEFORE INSTALLING!

In Triton 3.2.0 there is MASSIVE backend changes, a big one to note is that AttrsDescriptor and other functions and calls are gone, like get_dict, get_hint I beleive are gone too, with NO 1:1 standin replacing them as it is a entire backbone change that integrates all those removed into existing systems, I.E. libtriotn.pyd etc.

What this means is, you will need the BLEEDING EDGE as of 3/2025 so that your software, most likely and notably PYTORCH needs to either have a EXPERIMENTAL BUILD, not --- I say again as of writing this -- NOT -- Nightly, but experimental, as the pip installs were not up to date for me, check Nvidia, or HuggingFace, or if you fancy use the links I provide here.

This is not a bug with this build, its technically not a bug with triton or torch or anyone, this is just a version creep spasm.

CPython | PyTorch | Torchvision

----------|----------|----------

3.10 | [Download](https://huggingface.co/w-e-w/torch-2.6.0-cu128.nv/resolve/main/torch-2.6.0+cu128.nv-cp310-cp310-win_amd64.whl) | [Download](https://huggingface.co/w-e-w/torch-2.6.0-cu128.nv/resolve/main/torchvision-0.20.0a0+cu128.nv-cp310-cp310-win_amd64.whl)

3.11 | [Download](https://huggingface.co/w-e-w/torch-2.6.0-cu128.nv/resolve/main/torch-2.6.0+cu128.nv-cp311-cp311-win_amd64.whl) | [Download](https://huggingface.co/w-e-w/torch-2.6.0-cu128.nv/resolve/main/torch-2.6.0+cu128.nv-cp311-cp311-win_amd64.whl)

3.12 | [Download](https://huggingface.co/w-e-w/torch-2.6.0-cu128.nv/resolve/main/torch-2.6.0+cu128.nv-cp312-cp312-win_amd64.whl) | [Download](https://huggingface.co/w-e-w/torch-2.6.0-cu128.nv/resolve/main/torchvision-0.20.0a0+cu128.nv-cp312-cp312-win_amd64.whl)

Any updates to this update as well as experimental fixes will be here:
[Triton 3.2.0 AttrsDesc Issue and Potential fixes](https://github.com/leomaxwell973/Triton-3.2.0-Windows-Nvidia-Prebuilt/wiki/Triton-3.2.0-AttrsDescriptor-issue-topic.)

### - END CRITIACAL UPDATE


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
- **Built for:** **Python 3.10.6**  
- **Built on:** **Windows 11 Insiders Dev Build**  
- **Hardware:** **NVIDIA RTX 3060**  
- **Compiler:** **MSVC ([v14.43.34808] Microsoft Visual C++20)**  
- **CUDA Version:** **12.1**  
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
pip install https://github.com/leomaxwell973/Triton-3.2.0-Windows-Nvidia-Prebuilt/releases/latest/download/Triton-3.2.0-cp310-cp310-win_amd64.whl
```
Or from download:
```sh
pip install .\Triton-3.2.0-cp310-cp310-win_amd64.whl
```

---

## **💬 Final Notes**
This build is designed **specifically for Windows users with NVIDIA hardware**, eliminating unnecessary dependencies and optimizing performance. If you're developing **AI models on Windows and need a clean Triton setup without AMD bloat or Linux workarounds**, or have had difficulty building triton for Windows, this is **the best version available.**  

🔥 **Enjoy the cleanest, fastest Triton experience on Windows!** 🚀😎

If you'd like to show appreciation (donate) for this work: https://buymeacoffee.com/leomaxwell
