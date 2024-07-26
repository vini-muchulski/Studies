import requests, json, sys

country = "brazil"


schema = {"country": {"type": "string", "description": "Country name"},
          "capital": {"type": "string", "description": "Capital of the country"}}
          

payload = { "model": "llama3",
           "messages": [
             {"role": "system", "content": """You are a helpful AI assistant. The user will enter a country name and the assistant will return the capital of the country. Output in JSON.
              using the schema defined here: {schema}. For example, if the user enters "france", the assistant will return {"country": "france", "capital": "paris"}. """},
             {"role": "user", "content": f"I want to know the capital of {country}"}
             ],
           "options":{ "temperature":0.0},
           "format": "json"   
           }

response = requests.post("http://127.0.0.1:11434/api/chat", json=payload)

for message in response.iter_lines():
  jsonstr = json.loads(message)
  print(jsonstr["message"]["content"],end="")