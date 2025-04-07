'''
Let's write an LLM-based spellchecker!

The spellchecker should take some text as input and return the misspelled works along with suggestions for the correct spellings. 

Make the inputs, then create a suitable prompt for the LLM. 
#31

'''

import requests
import streamlit as st
import json

# write a wrapper function to call the LLM API
