#REGISTRATION FORM
import streamlit as st
st.header("Form registration")
with st.form("Form"):
    name=st.text_input("Enter your name: ")
    email=st.text_input("Enter your email: ")
    date = st.date_input("Enter date")
    check = st.checkbox("Click")
    button = st.form_submit_button("Submit")
if button:
    (name,email)
 
    

    