import pandas as pd
import numpy as np
import streamlit as st

link = 'https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv'

st.title('My first DataFrame')

customers = pd.read_csv(link)
choice = st.radio('Select Gender:', options= ['M', 'F']) # radio button 
cols = st.multiselect('Select Columns:', customers.columns) # select multiple columns
gender_index = customers["Gender"] == choice # filter dataframe based on gender 
st.dataframe(customers[gender_index][cols]) #display filtered dataframe based on gender selected





