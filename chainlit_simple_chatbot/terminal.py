import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")


while True :
    user_input = input ("Enter you question here or ('quit' to exit the application)")

    if user_input.lower() == 'quit':
        print ("Thanks for chatting !")
        break 
    response = model.generate_content(user_input)

    print (response.text)



# this is the code for chainlit ui with stateless bot (not integrated apikey )

# @cl.on_message
# async def  main (message:cl.Message):
#     response = f"You said {message.content}"
#     await cl.Message(content = response).send()