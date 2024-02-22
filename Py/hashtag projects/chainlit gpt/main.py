import chainlit as cl
import google.generativeai as genai
from keys import api_gemini

genai.configure(api_key=api_gemini)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    response = chat.send_message(message.content)
    print(message.content)
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response.text}",
    ).send()

    
