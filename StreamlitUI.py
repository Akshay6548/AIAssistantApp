import firebase_admin
import google.generativeai as genai
import streamlit as st
import datetime

# Access Firebase credentials as a dictionary
firebase_creds = dict(st.secrets["firebase"])
print(firebase_creds)

from firebase_admin import credentials, firestore

cred = credentials.Certificate(firebase_creds)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

# Access root-level secrets
gemini_key = st.secrets["gemini_api_key"]


genai.configure(api_key=gemini_key)
model = genai.GenerativeModel("gemini-pro")
for m in genai.list_models():
    print(m.name)


def get_response(prompt):
    response = model.generate_content(prompt)
    try:
        return response.candidates[0].content.parts[0].text
    except (IndexError, AttributeError):
        return "Sorry, I couldn't generate a response."


st.title("Personal AI Assistant")
user_input = st.text_input("Ask me anything:")
if st.button("Submit") and user_input:
    response = get_response(user_input)
    st.write("🤖:", response)

    # Save to Firestore
    
    db.collection("chat").add({
        "question": user_input,
    	"answer": response,
    	"timestamp": datetime.datetime.utcnow()
    })
