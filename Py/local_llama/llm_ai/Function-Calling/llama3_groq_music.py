from langchain_experimental.llms.ollama_functions import OllamaFunctions



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
    model="llama3-groq-tool-use", 
    format="json"
)

model = model.bind_tools(
    tools=[
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
            
            if tool_call['name'] == 'play_music':
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


#music_query = "Toque a musica de Stressed out de Twenty One Pilots"
#musica = "the man who sold the world de Nirvana"
musica = "eleanor rigby"
music_query = f"Toque a musica {musica}. - retorne o json com o artista "

print("\nResultado da consulta de música:")
print(process_request(music_query))