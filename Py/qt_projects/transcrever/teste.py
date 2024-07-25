
import torch

if torch.cuda.is_available():
    print("PyTorch is available on CUDA.")
else:
    print("PyTorch is not available on CUDA.")