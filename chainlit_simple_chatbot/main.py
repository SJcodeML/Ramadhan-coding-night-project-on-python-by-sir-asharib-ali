import chainlit as cl 
import os 
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key =  gemini_api_key )

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
 

@cl.on_chat_start
async def handle_start_chat():
    await cl.Message(content = "Hello !how can i help you today ?").send() 