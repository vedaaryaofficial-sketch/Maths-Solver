import streamlit as st
import google.generativeai as genai

st.title("Vedaarya Math Bot 🤖")

# Yeh 'secrets' se key uthayega
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Apna Math sawaal yahan likhein:")

if st.button("Solve"):
    prompt = f"You are a helpful math tutor for Vedaarya Academy. Solve this step-by-step: {user_input}"
    response = model.generate_content(prompt)
    st.write(response.text)
