#FIZZBUZZ GAME
import streamlit as st
st.header("Let's Play the Game")
number= st.number_input("Enter a number")
while number<=30:
    if number%3==0 and number%5 == 0:
        st.write("FizzBuzz")
        st.write(number)
    elif number%3 ==0:
        st.write("Fizz")
        st.write(number)
    elif number%5 == 0:
        st.write("Buzz")
        st.write(number)
    
    number+=1
        





