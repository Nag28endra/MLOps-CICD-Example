import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square and cube.")
number = st.number_input("Enter a number:", value=0)
square = number ** 2
cube = number ** 3
st.write(f"The square of {number} is {square}.")
st.write(f"The cube of {number} is {cube}.")