import pandas as pd
import numpy as np
import requests
import streamlit as st

response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")
employees = response.json()
st.write(employees) # this will show the dictionary

departments= []
for dept_name in employees.keys():
    dept_employees=pd.json_normalize(employees, record_path=dept_name)
    #st.write(dept_employees)
    dept_employees['dept']=dept_name
    departments.append(dept_employees)
    
    
combined = pd.concat(departments, ignore_index=True)
st.dataframe(combined)


    
 




