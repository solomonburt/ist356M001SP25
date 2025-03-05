import pandas as pd
import streamlit as st  
import numpy as np
import requests 


link = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json'

response= requests.get(link)
employees = response.json() # text convert to json
st.write(employees)
employees_df = pd.json_normalize(employees)
employees_df = pd.json_normalize(employees, record_path=['employees'], meta=['dept'])
st.dataframe(employees_df)