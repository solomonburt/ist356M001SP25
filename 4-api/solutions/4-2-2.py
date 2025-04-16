'''
Come up with a caching strategy for the Azure sentiment API. Use the `requests_cache.py` module. You will need to decided on the cache key.

For the following input:

for each text in the list:  
output the text, the sentiment, and if the results came from the API or cache.

Summary of the Process:
The script first attempts to load the sentiment results from a cache (sentiment.pkl).
If the text's sentiment is not cached, it sends a request to the sentiment analysis API.
The results are saved to the cache for future use.
The sentiment (positive, negative, or neutral) for each text is printed, along with whether the result was retrieved from the cache or generated via a new API call.


'''


import requests 
import requests_cache as rq # adds caching capabilities to requests


# sample texts to test
texts = [
    "I love IST356. It is the best course I've ever taken.", 
    "I hate the New York Giants.",
    "I love IST356. It is the best course I've ever taken.", 
    "I don't like the New York Giants."
]

cache = rq.clear_cache('sentiment.pkl') # clearing cache for the file named sentiment.pkl
apikey = "e4817f2223fc521129078fbf"
headers = { 'x-api-key': apikey }
url = "https://cent.ischool-iot.net/api/azure/sentiment"
for text in texts: # loop through each text in the list
    if text in cache: # checks if current text has been cached before . If cache found then uses the cached result
        results = cache[text] #retrieve the sentiment results from the cache
        from_cache = "CACHED" # if the text is in the cache, it is marked as CACHED
    else: # make a request to the API if the text is not in the cache
        data = { 'text': text } # text to be analyzed
        # make a POST request to the API with the text and headers      
        response = requests.post(url, headers=headers, data=data)
        results = response.json()
        cache[text] = results # results added ti the cache with the text as the key and results as values
        rq.save_cache(cache, 'sentiment.pkl') # cache saved to the file sentiment.pkl
        from_cache = "NOT CACHED" # if the text is not in the cache, it is marked as NOT CACHED

    sentiment = results['results']['documents'][0]['sentiment'] # extract the sentiment result from the API response
    print(text, sentiment, from_cache)