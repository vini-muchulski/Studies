import torch
import torchvision
# Verifica se o CUDA está disponível
cuda_disponivel = torch.cuda.is_available()

# Exibe o resultado
print(f"CUDA disponível: {cuda_disponivel}")

# Se o CUDA estiver disponível, exibe informações adicionais
if cuda_disponivel:
    # Obtém o nome do dispositivo CUDA
    nome_dispositivo = torch.cuda.get_device_name(0)

    # Obtém a versão do CUDA
    versao_cuda = torch.version.cuda

    # Exibe as informações
    print(f"Dispositivo CUDA: {nome_dispositivo}")
    print(f"Versão do CUDA: {versao_cuda}")

# Verifica a versão do PyTorch
versao_pytorch = torch.__version__

# Exibe a versão do PyTorch
print(f"Versão do PyTorch: {versao_pytorch}")



print(f"PyTorch version: {torch.__version__}")
print(f"Torchvision version: {torchvision.__version__}")

#pip install torchvision==0.18.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html
