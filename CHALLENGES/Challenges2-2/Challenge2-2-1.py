import streamlit as st


# setup
st.title("Rectangle Perimeter & Area")
length = st.number_input("What is the length?")
width = st.number_input("What is the width?")
calculate_clicked = st.button('Calculate')
clear_clicked = st.button('Clear')

if length not in st.session_state:
    st.session_state.length = 0
if width not in st.session_state:
    st.session_state.width = 0

if calculate_clicked:
    perimeter = 2 * (length + width)
    area = length * width
    st.write(f"Perimeter: {perimeter}")
    st.write(f"Area: {area}")
    
if clear_clicked:
    perimeter = None 
    area = None
    st.session_state.width = None
    st.session_state.length = None
    st.session
    st.rerun()

    






