import ollama

res = ollama.chat(
    model="llava:13b", #  model="llava:13b",
    messages=[
        {"role": "user", 
         "content": "descreva essa imagem ", #  em português
         "images": ["./img4.jpg"]},
    ]
)


print(res["message"]["content"])