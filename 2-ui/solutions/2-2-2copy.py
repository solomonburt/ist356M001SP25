import streamlit as st

# initialize session state
if 'total' not in st.session_state:
    st.session_state.total = 0.0
if 'amount' not in st.session_state:
    st.session_state.amount = 0.0


# Title and inputs and buttons
st.title('Order Total ')
amount = st.number_input("Amount:", value = st.session_state.amount)
col1, col2 = st.columns(2)
btn_add = col1.button('Add to Total')
btn_clear = col2.button('Clear')

# Add amount to total and history
if btn_add:
    st.session_state.total = st.session_state.total + amount
    st.write(f"TOTAL: {st.session_state.total}")


# Clear history and total. 
if btn_clear:
    st.session_state.total = 0.0
    st.session_state.amount = None
    st.rerun()
