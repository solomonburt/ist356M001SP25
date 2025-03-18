import pandas as pd
import streamlit as st

url ='https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'

#st.dataframe(df)


'''
Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection

'''

st.title ('Exam Scores Summary')

options = ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']
exams = pd.read_csv(url)
option =st.selectbox('Select an option', options)

summary = exams.groupby(option).agg({'Class_Section': 'count', 'Student_Score' :'mean'})
summary = summary.rename(columns = {'Class_Section':'Student_Count', 'Student_Score':'Average Score'})
st.dataframe(summary)




