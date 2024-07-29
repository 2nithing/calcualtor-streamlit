import streamlit as st

st.title('calculator')
num1 = st.number_input("enter the first number", value=0)
option = st.selectbox(
    "Select an action",
    ("+", "-", "x","/"),
)
num2 = st.number_input('enter the second number',value=0)
clicked = st.button('Submit')
if clicked:
    if option=="+":
        st.write("Answer is", num1+num2)
    if option=="-":
        st.write("Answer is", num1-num2)
    if option=="x":
        st.write("Answer is", num1*num2)
    if option=="/":
        st.write("Answer is", num1/num2)