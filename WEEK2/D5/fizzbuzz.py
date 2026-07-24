import streamlit as st
import httpx 

st.header("Let's Play the Game")

number = st.number_input("Enter a number", step=1, value=1)

while number <= 30:
    if number % 3 == 0 and number % 5 == 0:
        st.write("FizzBuzz")
        st.write(number)
    elif number % 3 == 0:
        st.write("Fizz")
        st.write(number)
    elif number % 5 == 0:
        st.write("Buzz")
        st.write(number)
    number += 1

if st.button("Numbers"):
    try:
        response = httpx.get("http://localhost:8000/numbers")
        response.raise_for_status()
        numbers = response.json()
        st.session_state['numbers_data'] = numbers
        
    except Exception as e:
        st.error(f"Failed to find numbers: {e}")

if 'numbers_data' in st.session_state and st.session_state.numbers_data:
    st.divider()
    st.subheader("Numbers from FastAPI")
    
    st.write(st.session_state.numbers_data)
