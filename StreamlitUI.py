import streamlit as st

st.title("Personal AI Assistant")

user_input = st.text_input("Ask me anything:")
if user_input:
    response = get_response(user_input)
    st.write("🤖:", response)

    # Save to Firestore
    db.collection("chat").add({"question": user_input, "answer": response})