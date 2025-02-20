import streamlit as st

st.title("Area and Perimeter .")
length = st.number_input("Enter the length")
width = st.number_input("Enter the width")
btn_clicked = st.button("Calculate")



if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")
    