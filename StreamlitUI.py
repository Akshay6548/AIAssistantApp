import firebase_admin
import google.generativeai as genai
import streamlit as st

# Access Firebase credentials as a dictionary
firebase_creds = dict(st.secrets["firebase"])

from firebase_admin import credentials, firestore

cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Access root-level secrets
gemini_key = st.secrets["gemini_api_key"]


genai.configure(gemini_key)
model = genai.GenerativeModel("gemini-pro")

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text
st.title("Personal AI Assistant")

user_input = st.text_input("Ask me anything:")
if user_input:
    response = get_response(user_input)
    st.write("🤖:", response)

    # Save to Firestore
    db.collection("chat").add({"question": user_input, "answer": response})