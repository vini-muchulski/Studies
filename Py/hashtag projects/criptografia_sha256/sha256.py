# -*- coding: utf-8 -*-
"""sha256

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O4p6ADE1SJqwQE5ti_flQIv-GtZ1D-tN
"""

from hashlib import sha256
# https://www.youtube.com/watch?v=HWdMKrtTgdM&

nome = "vini".encode()
print(nome, type(nome))

senha = "1234abc"
                  # o texto deve estar em formato de bytes  -> usar encode para isso
hash_senha = sha256(senha.encode())

#print(hash_senha)
#print(hash_senha.digest())

senha_criptografada = hash_senha.hexdigest()
print(senha_criptografada)