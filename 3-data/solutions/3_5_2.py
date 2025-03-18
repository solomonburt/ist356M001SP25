'''
https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv

Let's build an interactive pivot table in streamlit!

- create a row and column selection widgets allowing the user to select one of the following columns:  
`'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
- create a measure column selestion widget which allows the user to select one of these columns:  
`'Completion_Time','Student_Score'`
- build the pivot table dataframe from the inputs. use the average for the `aggfunc`
- display the pivot table!

'''
import pandas as pd
import streamlit as st


url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv"

st.title('Exam Scores Pivot Table')

cols = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
measures = ['Completion_Time','Student_Score']
exams = pd.read_csv(url)


row = st.selectbox('Select a row', cols)
cols.remove(row)
col = st.selectbox('Select a column', cols)
value = st.selectbox('Display the Average', measures)

pivot_df = exams.pivot_table(index=row, columns=col, values=value, aggfunc='mean')
st.dataframe(pivot_df)
