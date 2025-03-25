import streamlit as st
import random 
import time
import requests

# url of the deployed application 
# https://money-making-machine-and-usage-of-apis-by-sidra-jabin.streamlit.app/


def generate_money():
    return random.randint(1 , 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money")
    time.sleep(2)
    amount = generate_money()
    st.success(f"You have made ${amount}")



def get_side_hustle():
    try:
        # response =requests.get("http://127.0.0.1:8000/side_hustles?apikey=123456789")
        response =requests.get("https://ramadhan-coding-night-project-on-python-by-sir-asharib-ali.vercel.app/side_hustles?apikey=123456789")
        if response.status_code == 200:
            hustles= response.json()
            return hustles["side_hustle"]    
    except:
        return ("Somehing went wrong!")
    

st.subheader("Side Hustle Ideas")

if st.button ("Generate Hustle"):
    idea = get_side_hustle()
    st.success(idea)



def get_money_quotes():
    try:
        # you need to deploy this api on the server then it will work otherwise you need to activate an run the api key from the project 
        # in next projects we will deploy this key then may be it will work check it 

        # response = requests.get("http://127.0.0.1:8000/money_quotes?apikey=123456789")  this is the URl without deploying on vercel 
        response = requests.get("https://ramadhan-coding-night-project-on-python-by-sir-asharib-ali.vercel.app/money_quotes?apikey=123456789") 
        # above url after deploying on vercel from fast-api project and url's are written in deployment_vercel project
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
    except:
        return ("Something went wrong")

st.subheader("Money_Making_Quotes")

if st.button("Generate Quotes"): 
  quotes = get_money_quotes()
  st.success(quotes)       
       