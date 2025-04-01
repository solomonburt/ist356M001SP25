'''
Use the IoT portal for the URI to search for funny names. Once you understand how to invoke the REST API, write a streamlit to 
input a name and return the matches in a dataframe. 
'''


import pandas as pd
import requests
import streamlit as st

st.title("Funny Name Search")

uri = "https://cent.ischool-iot.net/api/funnyname/search"
search = st.text_input("Search for a name")
if st.button("Search"):
    response = requests.get(uri, params={"q": search})
    response.raise_for_status() #raise an error if the request failed
    data = response.json()
    #st.write(data)
    
    df = pd.DataFrame(data)
    st.dataframe(df)