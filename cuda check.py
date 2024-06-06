import torch

# Check if CUDA is available
cuda_available = torch.cuda.is_available()

# Get the number of CUDA devices available
cuda_device_count = torch.cuda.device_count()

# Check for device 0 and 1
device_0_available = cuda_device_count > 0
device_1_available = cuda_device_count > 1

print(f"CUDA Available: {cuda_available}")
print(f"Device 0 Available: {device_0_available}")
print(f"Device 1 Available: {device_1_available}")

# If both devices are available, print their names
if device_0_available:
    print(f"Device 0 Name: {torch.cuda.get_device_name(0)}")
if device_1_available:
    print(f"Device 1 Name: {torch.cuda.get_device_name(1)}")
