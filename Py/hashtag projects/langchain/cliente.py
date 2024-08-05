from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/tradutor")
texto = chain_remota.invoke({"idioma":"portugues","texto":"fale sobre o que foi a apollo 11"})
print(texto)