import triton
from triton.testing import do_bench

# Define a function that uses Triton
def my_function():
    # Your Triton kernel code here
    pass

# Benchmark the function
runtime = do_bench(my_function)
print(f"Runtime: {runtime} ms")