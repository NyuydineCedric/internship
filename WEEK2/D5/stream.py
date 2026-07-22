import streamlit as st
import random
with st.sidebar:
    st.title("Hello")
    st.header("NEw")
st.write("Hello")
secret = 8
numbers = [1,2,3,4,5,6,7,8,9,10]

button = st.button("Click")
if button:
    
    number  = st.number_input("Enter a guess number")
# for number in numbers:
    if number>secret:
        st.write("High")
    elif number<secret:
        st.write("Low")
    else:
        st.write("Correct")
    
        
    
    
