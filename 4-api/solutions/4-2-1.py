'''
For this challenge, use Azure entity recognition API to extract entities from the following text.

"The Dallas Cowboys are a far better team than the New York Giants this year. The Giants have not won a conference game yet."

Using the API output, print each extracted entity and its type.

curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: e4817f2223fc521129078fbf' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=today%20is%20sunny%20in%20syracuse'


'''
import pandas as pd
import numpy as np

import streamlit as st
import requests
import json 

def extract_entities(text: str)->dict:
    '''
    Extract entities from the text using Azure entity recognition API.
    '''
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    data = {'text': text}
    headers={'X-API-KEY': 'USE YOUR OWN API KEY'}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()

text = st.text_area("Enter text to extract entities:")
if text:
    result = extract_entities(text)
    entities = result ['results']['documents'][0]['entities'] 
    df = pd.DataFrame(entities)
    st.dataframe(df)  



    
        
