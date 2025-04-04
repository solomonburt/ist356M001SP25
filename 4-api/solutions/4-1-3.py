'''
Figure out how to call these in the IoT portal:
- Google geocode API to take a location and get a latitute and longitude
- Weather API to get the weather for a latitude and longitude

Write a streamlit to input a location and return the current weather conditions. Use the `st.metric` to display the temperature and humidity with units. e.g. 56°F and 80% humidity.


curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial%20&lon=-76&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: e4817f2223fc521129078fbf'
  
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse%2C%20ny' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: e4817f2223fc521129078fbf'


'''

# imports
import pandas as pd
import numpy as np  
import streamlit as st
from time import sleep

import requests
import json

st.title("Weather ☁️ API")
location = st.text_input("Enter a location to get the weather:")
if st.button("Get Weather"):
    with st.spinner("Fetching weather data..."):
        sleep(2)
        # st.success("Done!")
        url = "https://cent.ischool-iot.net/api/google/geocode"
        querystring = {"location": location}
        headers ={'X-API-KEY': 'e4817f2223fc521129078fbf'}
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        geocode = response.json()
        #st.write(geocode)
        lon = geocode ["results"][0]["geometry"]["location"]["lng"]
        lat = geocode ["results"][0]["geometry"]["location"]["lat"]
        
        
        url = "https://cent.ischool-iot.net/api/weather/current"
        querystring = {"units": "imperial", "lon": lon, "lat": lat}
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        weather = response.json()
        #st.write(weather)
        temp = weather['current']['temperature_2m']
        st.metric(label="Temperature", value=f"{temp}°F")
        
   


