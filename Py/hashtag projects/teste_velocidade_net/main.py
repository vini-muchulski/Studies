import speedtest

teste = speedtest.Speedtest()

print("iniciando testes...")
#download
velocidade_download = teste.download()
velocidade_download

#upload
velocidade_upload = teste.upload()

# ping
ping = teste.results.ping

print(f"Velocidade de Download: {(velocidade_download / (1024*1024)):.2f} Mbps")
print(f"Velocidade de Upload: {(velocidade_upload / (1024*1024)) :.2f} Mbps")
print(f"Ping: {ping }")