'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'
  
'''

import requests
url = "https://cent.ischool-iot.net/api/funnyname/random"
querystring = {"n":"3"} #
response = requests.get(url, params=querystring)


#if response.ok:
#print(response.text)
print(response.url)



response.raise_for_status() #raise an error if the request failed

#names = response.json()
#for name in names:
    #print(name['first_name'], name['last_name'])