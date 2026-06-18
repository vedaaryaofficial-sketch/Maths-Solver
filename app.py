import streamlit as st
import google.generativeai as genai

st.title("Vedaarya Math Bot 🤖")

# API KEY ko yahan quotes ke andar seedha paste karein
api_key = "AQ.Ab8RN6JX-41G3dVA-i0ouNHiC8kTO_07fuKGCIz1JtApqIh23w" 

genai.configure(api_key=api_key)

# Model configuration
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Apna Math sawaal yahan likhein:")

if st.button("Solve"):
    if not api_key or api_key == "PASTE_YOUR_API_KEY_HERE":
        st.error("API Key missing! Code mein apni key daalein.")
    else:
        try:
            prompt = f"You are a helpful math tutor for Vedaarya Academy. Solve this step-by-step: {user_input}"
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error aaya hai: {e}")
