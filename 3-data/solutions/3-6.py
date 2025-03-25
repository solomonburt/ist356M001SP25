'''
- Build a data pipeline to read in the roster and poll responses then create this dataset:
    - student information
    - date of polling session
    - number of polls during session
    - number of polls student answered during session
    - label indicating if the student was absent or non participant

- streamlit UI where you can select a student and see their polling data and grade

- from the dataset, generate a CSV file for upload into for X-Menboard LMS:
    - one row per student
    - total class sessions
    - total absences AB
    - total non-participant np
    - pct of sessions AB or np

'''

import pandas as pd
import streamlit as st

# Load the roster and 
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls"
roster_df = pd.read_csv(f"{base}/roster.csv")
st.dataframe(roster_df)

