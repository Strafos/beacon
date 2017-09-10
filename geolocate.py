import requests
import json
import nltk
import info

bias = True
bias_loc = 'Pennsylvania'
def geolocate(location):
    if location is None:
        return
    print(location)
    location_words = nltk.word_tokenize(location)
    if bias:
        for i in range(len(location_words)):
            if location_words[i] in info.US_states:
                location_words[i] = ''
        location_words.append(bias_loc)
        print(location_words) 
    API_KEY = 'AIzaSyA6R-TFHRYb2jh2gpJF6vfnSr3uZZlxzEs'
    request_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    for i in range(len(location_words)):
        if i is not 0:
            request_url = request_url + '+'
        request_url = request_url + location_words[i]
    request_url = request_url + '&key=' + API_KEY
    r = requests.get(request_url)
    jsond = json.loads(r.text)
    if(len(jsond["results"]) is 0):
        return [0,0]
    lat = (jsond["results"][0]["geometry"]["location"]["lat"])
    lng = (jsond["results"][0]["geometry"]["location"]["lng"])
    print(('{0}, {1}').format(lat, lng))
    return [lat, lng]

geolocate('47 Chestnut')