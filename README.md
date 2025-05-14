# **Triton (~V3.2.0~ V3.3.0) Windows Native Build – NVIDIA Exclusive**
UPDATED to 3.3.0 
# ADDED 312 POWER!
~Note: this is for python 3.10(.6(?)), I was under the false impression i had labled it better, well, my bad. package says so but, i have no intention at this time unless there is actuall demand for other versions iee py311 or py312 etc. as ive not had a need want or reason to use those and so makes no sense to do so at this time for me until i either need it, or some large-scale use case demand is brought to my attention.~
Well that didn't take long, this repo is now/for-now Py310 and Py312!

# Check Releases for the latest most likely bug free version!
## Broken versions will be labeled

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
This version, last I checked, is for bypassing apps with a linux/unix/posix focus platform, but have nothing that makes them strictly so, and thus, had triton as a no-worry reqirement on a supported platform sich as them, but no regard for windows, despite being compatible for them regardless. Or such case uses.
It's a shell of triton, vaporware, that provides only token comparions of features or gpu enhancment compared to the full version of linux.
THIS REPO - Is such a full version, with llvm and nothing taken out as long as its not involving AMD GPUs.

🔥 **Enjoy the cleanest, fastest Triton experience on Windows!** 🚀😎

If you'd like to show appreciation (donate) for this work: https://buymeacoffee.com/leomaxwell
