import streamlit as st 

def convert_units(value,unit_to, unit_from):

    conversions = {  
         "meters_kilometers": 0.001,  
         "kilometers_meters": 1000,  
         "grams_kilograms": 0.001,  
         "kilograms_grams": 1000  
     } 

    key =f"{unit_from}_{unit_to}"

    if key in conversions :
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"


st.title("Unit converter")

value = st.number_input("Enter you value" , min_value=1.0 , step = 1.0)

unit_from = st.selectbox("Convert From:", ["meters", "kilometers", "grams", "kilograms"])  
unit_to = st.selectbox("Convert To:", ["meters", "kilometers", "grams", "kilograms"])  



if st.button("Convert"):
    result = convert_units(value,unit_to,unit_from )
    st.write(f"Converted value: {result}")
 









# import streamlit as st   

# def convert_units(value, unit_to, unit_from):  
#     conversions = {  
#         "meters_kilometers": 0.001,  
#         "kilometers_meters": 1000,  
#         "grams_kilograms": 0.001,  
#         "kilograms_grams": 1000  
#     }  

#     key = f"{unit_from}_{unit_to}"  

#     if key in conversions:  
#         conversion = conversions[key]  
#         return value * conversion  
#     else:  
#         return "Conversion not supported"  

# st.title("Unit Converter")  

# value = st.number_input("Enter your value:")  
# unit_from = st.selectbox("Convert From:", ["meters", "kilometers", "grams", "kilograms"])  
# unit_to = st.selectbox("Convert To:", ["meters", "kilometers", "grams", "kilograms"])  

# if st.button("Convert"):  
#     result = convert_units(value, unit_to, unit_from)  
#     st.write(f"Converted value: {result}")  