import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(page_title="Vedaarya Math Bot")
st.title("Vedaarya Math Bot 🤖")
st.subheader("Apna sawaal pucho aur seekho!")

# API Key dalne ki jagah
api_key = st.text_input("Enter your API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_input = st.text_input("Maths problem likhein:")
    if st.button("Solve"):
        prompt = f"You are a helpful math tutor for Vedaarya Academy. Solve step-by-step: {user_input}"
        response = model.generate_content(prompt)
        st.write(response.text)
