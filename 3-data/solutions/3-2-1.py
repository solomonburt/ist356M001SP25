'''
Read this file into a pandas dataframe:

[https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log](https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log)

- What is the delimiter?
- is there a header? Which row?
- Do you need to skip lines?

Display only data where the time taken > 500 (msec) and the sc-status is 200

as a streamlit app

'''

import streamlit as st  
import pandas as pd
import numpy as np

link = 'https://raw.githubusercontent.com/mafudge/datasets/master/delimited/webtraffic.log'
st.title('Web Traffic Log Analysis')

wt = pd.read_csv(link, sep='\s+',  skiprows=3, header= 0)

# Filtering 

wt_filter = (wt['sc-status'] == 200) & (wt['time-taken'] > 500)
wt_slow_but_successful = wt[wt_filter]
st.dataframe(wt_slow_but_successful) # first 20 rows by default



