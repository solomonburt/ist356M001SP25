import requests 
import requests_cache as rq
# requests_cache library caches 


texts = [
    "I love IST356. It is the best course I've ever taken.", 
    "I hate the New York Giants.",
    "I love IST356. It is the best course I've ever taken.", 
    "I don't like the New York Giants."
]

# creates a new cache file  or deletes the existing one, starting with an empty cache
cache = rq.clear_cache('sentiment.pkl')
apikey = "YOUR API KEY HERE"
headers = { 'x-api-key': apikey }
url = "https://cent.ischool-iot.net/api/azure/sentiment"
for text in texts: # loop over each text string in the list
    if text in cache: # check if the text is already in the cache
        # if it is, retrieve the results from the cache
        results = cache[text]
        from_cache = "CACHED"
    # if it is not, make a request to the API and store the results in the cache
    # and save the cache to a file
    else:
        data = { 'text': text } # create a dictionary with the text to be analyzed
        # make a POST request to the API with the text and headers
        response = requests.post(url, headers=headers, data=data)
        results = response.json()
        cache[text] = results
        rq.save_cache(cache, 'sentiment.pkl') # save the cache to file for future runs
        from_cache = "NOT CACHED"

    sentiment = results['results']['documents'][0]['sentiment']
    print(text, sentiment, from_cache)