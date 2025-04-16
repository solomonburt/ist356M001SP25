import streamlit as st

if 'total' not in st.session_state:
    st.session_state.total = 0.0
    
if 'history' not in st.session_state:
    st.session_state.history = []

if 'amount' not in st.session_state:
    st.session_state.amount = 0.0

# setup
st.title("Order Total/History")
row1, row2 = st.columns(2)
amount = st.number_input("What is the amount of your order?", value = st.session_state.amount)
with row1:
    accumulate_clicked = st.button('Accumulate')
with row2:
    clear_clicked = st.button('Clear')



if accumulate_clicked:
    st.session_state.history.append(amount)
    st.session_state.total = sum(st.session_state.history)
    st.write(f"Total: {st.session_state.total}")
    st.write(f"Your Entry History: {st.session_state.history}")
    
    
if clear_clicked:
    amount = None
    st.session_state.amount = None
    st.session_state.history = []
    st.session_state.total = None
    st.rerun()