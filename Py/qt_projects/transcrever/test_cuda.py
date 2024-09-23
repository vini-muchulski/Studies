import torch

#https://github.com/openai/whisper/discussions/1185

if torch.cuda.is_available():
    print("PyTorch is available on CUDA.")
else:
    print("PyTorch is not available on CUDA.")