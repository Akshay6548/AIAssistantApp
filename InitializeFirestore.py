import firebase_admin
import streamlit as st

# Access Firebase credentials as a dictionary
firebase_creds = dict(st.secrets["firebase"])

from firebase_admin import credentials, firestore

cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred)
db = firestore.client()