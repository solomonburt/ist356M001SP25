'''
FirstGPT


'''

import requests
import streamlit as st

def get_text_responses(query:str) -> str:
    '''
    Call Genai and return a response.
    '''
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query": query}
    headers = {
        "X-API-KEY": "e4817f2223fc521129078fbf",
    }
    response = requests.post(url, data =data, headers=headers)
    response.raise_for_status()
    return response.json()


st.title("FirstGPT")

text = st.text_input("Enter a text to get a response:")
if text:
    response = get_text_responses(text)
    st.write(response)
    