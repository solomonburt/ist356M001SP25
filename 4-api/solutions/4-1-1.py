'''
Write a streamlit to read from the url:

https://jsonplaceholder.typicode.com/users/

Then display the data in a pandas dataframe. 

 - use the requests library to get the data
 - use `json_normalize()` to convert the nested json data into a dataframe

'''

# imports
import pandas as pd
import numpy as np
import streamlit as st
import requests


st.title("API Example to Pandas DataFrame")

uri ="https://jsonplaceholder.typicode.com/users/"
response = requests.get(uri)
response.raise_for_status() #raise an error if the request failed
data = response.json()
st.write(data)


df = pd.json_normalize(data)
st.dataframe(df)