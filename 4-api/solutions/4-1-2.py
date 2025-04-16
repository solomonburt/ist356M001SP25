'''
Use the IoT portal for the URI to search for funny names. Once you understand how to invoke the REST API, write a streamlit to 
input a name and return the matches in a dataframe. 

curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/search?q=an' \
  -H 'accept: application/json'


'''


import pandas as pd
import requests
import streamlit as st

st.title("Funny Name Search")

url = "https://cent.ischool-iot.net/api/funnyname/search"
search = st.text_input("Enter a name to search for funny names:")
if st.button("Search"):
    response = requests.get(url, params={"q": search})
    data = response.json()
    response.raise_for_status
    df = pd.DataFrame(data)
    st.dataframe(df)
