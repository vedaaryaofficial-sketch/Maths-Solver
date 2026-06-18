import streamlit as st
import google.generativeai as genai

st.title("Vedaarya Math Bot 🤖")

# Apni API KEY yahan daalein (Bina space ke)
api_key = "AQ.Ab8RN6Io-xAGUPNvx2OF2JqwsS9WfWB-b-4r9PDqSIDPRNf7oQ"

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Apna Math sawaal yahan likhein:")

if st.button("Solve"):
    prompt = f"You are a helpful math tutor for Vedaarya Academy. Solve this step-by-step: {user_input}"
    response = model.generate_content(prompt)
    st.write(response.text)
