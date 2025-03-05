import pandas as pd
import numpy as np
import requests
import streamlit as st

response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")
employees = response.json()
st.write(employees) # this will show the dictionary

df = pd.DataFrame(employees['accounting'])
st.dataframe(df)

for key in employees.keys():
    st.write(f"Key: {key}")


st.write(employees) # this will show the dictionary