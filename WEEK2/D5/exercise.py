import streamlit as st
import httpx

st.header("Form registration")

if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "email": ""}

with st.form("Form"):
    st.text_input(
        "Enter your name: ",
        key="name_input",
        value=st.session_state.user_data.get("name", "")
    )
    st.text_input(
        "Enter your email: ",
        key="email_input",
        value=st.session_state.user_data.get("email", "")
    )
    st.checkbox("I agree to the terms", key="agree")

    submitted = st.form_submit_button("Submit")

    if submitted:
        name = st.session_state.name_input
        email = st.session_state.email_input
        agree = st.session_state.agree
        if name and email and agree:
            st.success(f"Registered {name} with email {email}")
        else:
            st.error("Please fill all fields and accept the terms.")

if st.button("Load User"):
    try:
        response = httpx.get("http://localhost:8000/user")
        response.raise_for_status()
        user = response.json()
        st.session_state.user_data = user


    except Exception as e:
        st.error(f"Failed to fetch user: {e}")

if st.session_state.user_data.get("name") and st.session_state.user_data.get("email"):
    st.divider()
    st.subheader("Users")
    st.write(f"**Name:** {st.session_state.user_data['name']}")
    st.write(f"**Email:** {st.session_state.user_data['email']}")