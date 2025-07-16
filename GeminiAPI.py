import google.generativeai as genai
import streamlit as st

# Access root-level secrets
gemini_key = st.secrets["gemini_api_key"]


genai.configure(gemini_key)
model = genai.GenerativeModel("gemini-pro")

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text
