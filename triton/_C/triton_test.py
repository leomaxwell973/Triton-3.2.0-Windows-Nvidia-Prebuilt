import torch
import triton
import triton.language as tl

@triton.jit
def simple_kernel(output, n_elements, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    mask = offsets < n_elements
    
    # Just write a constant value
    tl.store(output + offsets, 42.0, mask=mask)

def test_simple():
    # Define output tensor
    n_elements = 1024
    output = torch.zeros(n_elements, device='cuda')
    
    # Define grid
    grid = (n_elements + 128 - 1) // 128
    
    # Launch kernel
    simple_kernel[(grid,)](output, n_elements, BLOCK_SIZE=128)
    
    # Verify results
    expected = torch.full((n_elements,), 42.0, device='cuda')
    success = torch.allclose(output, expected)
    print(f"Test passed: {success}")
    
    return output, success

if __name__ == "__main__":
    print("CUDA available:", torch.cuda.is_available())
    print("Testing simple Triton kernel...")
    output, success = test_simple()
    if success:
        print("First few elements:", output[:5])