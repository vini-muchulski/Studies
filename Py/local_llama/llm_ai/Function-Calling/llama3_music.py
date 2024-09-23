import requests
from typing import Optional
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.messages import HumanMessage
from keys import OPENWEATHERMAP_API_KEY

def get_current_weather(location: str, unit: Optional[str] = "celsius"):
    """
    Obtém o clima atual para uma localização específica.
    
    :param location: A cidade e estado, ex: "São Paulo, SP"
    :param unit: A unidade de temperatura (celsius ou fahrenheit)
    :return: Um dicionário com informações sobre o clima
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric" if unit == "celsius" else "imperial"
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "location": f"{data['name']}, {data['sys']['country']}",
            "temperature": data['main']['temp'],
            "unit": "°C" if unit == "celsius" else "°F",
            "description": data['weather'][0]['description']
        }
    else:
        return {"error": f"Unable to fetch weather data. Status code: {response.status_code}"}

def play_music(song_name: str, artist: str = None):
    """
    Simula a reprodução de uma música.
    
    :param song_name: Nome da música a ser tocada
    :param artist: Nome do artista (opcional)
    :return: Uma mensagem indicando a música que está sendo tocada
    """
    if artist:
        return f"Tocando '{song_name}' de {artist}."
    else:
        return f"Tocando '{song_name}'."

model = OllamaFunctions(
    model="llama3", 
    format="json"
)

model = model.bind_tools(
    tools=[
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["location"],
            },
        },
        {
            "name": "play_music",
            "description": "Play a song from the music library",
            "parameters": {
                "type": "object",
                "properties": {
                    "song_name": {
                        "type": "string",
                        "description": "The name of the song to play",
                    },
                    "artist": {
                        "type": "string",
                        "description": "The name of the artist (optional)",
                    },
                },
                "required": ["song_name"],
            },
        }
    ],
)

def process_request(query):
    # Obter a resposta do modelo
    response = model.invoke(query)
    print("Resposta do modelo:", response)

    # Extrair os parâmetros da resposta do modelo
    try:
        # Verificar se há tool_calls na resposta
        if hasattr(response, 'tool_calls') and response.tool_calls:
            tool_call = response.tool_calls[0]  # Assumindo que queremos o primeiro tool call
            print(f"Tool call: {tool_call}")  # Adicionar depuração
            if tool_call['name'] == 'get_current_weather':
                args = tool_call['args']
                print(f"Weather args: {args}")  # Adicionar depuração
                location = args.get('location')
                if not location:
                    return "Erro: Localização não fornecida para a previsão do tempo."
                unit = args.get('unit', 'celsius')
                
                # Chamar a função real para obter o clima
                weather_data = get_current_weather(location, unit)
                
                if 'error' in weather_data:
                    return f"Erro ao obter dados do clima: {weather_data['error']}"
                
                return f"O clima atual em {weather_data['location']} é {weather_data['temperature']}{weather_data['unit']} com {weather_data['description']}."
            
            elif tool_call['name'] == 'play_music':
                args = tool_call['args']
                print(f"Music args: {args}")  # Adicionar depuração
                song_name = args['song_name']
                artist = args.get('artist')
                
                # Chamar a função real para tocar a música
                return play_music(song_name, artist)
        else:
            return "Não foi possível interpretar a solicitação."
        
    except Exception as e:
        return f"Desculpe, não foi possível processar sua solicitação. Erro: {str(e)}"

# Exemplos de uso
weather_query = "Qual é o clima em São Paulo hoje?"
#music_query = "Toque a musica de Stressed out de Twenty One Pilots"
music_query = "Toque a musica radio ga ga - qual o artista? "
#print("Resultado da consulta de clima:")
#print(process_request(weather_query))
print("\nResultado da consulta de música:")
print(process_request(music_query))