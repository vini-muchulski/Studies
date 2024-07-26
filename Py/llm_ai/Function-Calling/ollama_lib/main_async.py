import ollama
import asyncio
from funcao_clima import get_current_weather

async def run():
    client = ollama.AsyncClient()
    messages = [{'role': 'user', 'content': 'What is the temperatura in Ararangua?'}]

    response = await client.chat(
        model='llama3.1',
        messages=messages,
        tools=[{
            'type': 'function',
            'function': {
                'name': 'get_current_weather',
                'description': 'Get the current weather for a city',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'city': {
                            'type': 'string',
                            'description': 'The name of the city',
                        },
                    },
                    'required': ['city'],
                },
            },
        }],
    )

    messages.append(response['message'])

    if response['message'].get('tool_calls'):
        for tool in response['message']['tool_calls']:
            if tool['function']['name'] == 'get_current_weather':
                city = tool['function']['arguments']['city']
                weather_info = get_current_weather(city)
                messages.append({
                    'role': 'tool',
                    'content': weather_info + "responda em portugues",
                })

    final_response = await client.chat(model='llama3.1', messages=messages)
    print(final_response['message']['content'])

asyncio.run(run())