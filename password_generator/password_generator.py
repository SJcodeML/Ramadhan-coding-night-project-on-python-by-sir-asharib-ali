
import random
import streamlit as st

chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


number = st.number_input("How many passwords you wanna generate: " , min_value=1.0 ,max_value=100.00,)

length = st.number_input("Enter your password length: " ,min_value=6.0, max_value=64.00 , step=1.0)
st.write("Here are your passwords")

# for pwd in range(number):
#    passwords=''
#    for c in range(length):
#     passwords += random.choice(chars)
#     print(passwords)

if st.button("Generate Password"):
  st.text("Here is your Password")
  for pwd in range(int(number)):
   passwords=''
   for c in range(int(length)):
     passwords += random.choice(chars)
   st.text(passwords)

       