import torch
import triton
import triton.language as tl

# **Check if CUDA is available**
assert torch.cuda.is_available(), "🔥 ERROR: CUDA is NOT available!"

# **Print GPU info**
print("🔥 CUDA Device:", torch.cuda.get_device_name(0))

# **Try to manually import the backend**
try:
    from triton.runtime import driver
    print("✅ Triton runtime loaded successfully!")
except Exception as e:
    print("🔥 Triton backend failed to load:", e)

# **Simple test kernel**
@triton.jit
def add_kernel(X, Y, OUT, N: tl.constexpr):
    idx = tl.program_id(0)
    if idx < N:
        x_val = tl.load(X + idx)
        y_val = tl.load(Y + idx)
        tl.store(OUT + idx, x_val + y_val)

# **Allocate memory**
N = 1024
X = torch.ones(N, dtype=torch.float32, device="cuda")
Y = torch.ones(N, dtype=torch.float32, device="cuda")
OUT = torch.empty(N, dtype=torch.float32, device="cuda")

# **Print before launching the kernel**
print("🔥 Launching Triton kernel...")

try:
    add_kernel[(N,)](X, Y, OUT, N=N)
    print("✅ Kernel launched successfully!")
except Exception as e:
    print("🔥 ERROR: Kernel failed to launch:", e)

# **Verify output**
if torch.all(OUT == 2):
    print("✅ Success! Triton kernel works!")
else:
    print("🔥 Failed! Output does not match expected value.")
