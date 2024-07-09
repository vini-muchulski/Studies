import ollama

res = ollama.chat(
    model="llava:13b", #  model="llava:13b",
    messages=[
        {"role": "user", 
         "content": "gere 5 palavras-chave descrevendo essa imagem (separado por virgula)", #  em português
         "images": ["./img3.jpg"]},
    ]
)


print(res["message"]["content"])