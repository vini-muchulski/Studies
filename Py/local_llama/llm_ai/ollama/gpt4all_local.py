from pathlib import Path
from gpt4all import GPT4All
import os

#To prevent GPT4All from accessing online resources, instantiate it with allow_download=False.
# model = GPT4All('ggml-mpt-7b-chat.bin', allow_download=False)
model_name = "mistral-7b-instruct-v0.1.Q4_0.gguf"
model_path = Path(os.environ['LOCALAPPDATA']) / 'nomic.ai' / 'GPT4All'
model = GPT4All(model_name, model_path)


output = model.generate("The capital of United States is ")
print(output)

output = model.generate("How was Alber Einstein? ")
print(output)

output = model.generate("What was the general theory? ")
print(output)