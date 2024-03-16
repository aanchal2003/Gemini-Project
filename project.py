from dotenv import load_dotenv
load_dotenv() #loading all the environment variable
from PIL import Image

import pandas as pd
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini and gemini pro model to get response
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
        print(response.text)
    response_text = response.text.strip()
    if response_text in df.iloc[:, 0].values:   
        st.write("The image data is registered in the dataset.")
    else:
        st.write("The image data is not registered in the dataset.")
        
    return response.text



##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input: ",key="input")
df = pd.read_csv('NUM_PLT.csv')  
st.write(df)
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

submit=st.button("Tell me about the image")


if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is")
    st.write(response)