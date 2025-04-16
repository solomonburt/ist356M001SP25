'''
A simple web application that allows users to input text and get a 
summarized version from an AI model running on a local server.

'''

import streamlit as st  
import requests

#Points to API endpoint running on your local machine (localhost) at port 8000. 
# The /tldr part is responsible for "Too Long; Didn't Read" (TLDR) style summarization.
url = "http://localhost:8000/tldr"

st.title("AI Text Summarizer")
text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    with st.spinner("Summarizing..."):
        response = requests.post(url, json={"text": text})
        response.raise_for_status()
        st.write(response.json())