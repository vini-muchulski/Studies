# status ollama http://localhost:11434
#lista modelos https://github.com/ollama/ollama

import ollama


stream = ollama.chat(
    model="gemma:2b" ,
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)


for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)