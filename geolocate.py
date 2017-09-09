import requests
import json
import nltk

def geolocate(location):
    if location is None:
        return
    location_words = nltk.word_tokenize(location)
    API_KEY = 'AIzaSyA6R-TFHRYb2jh2gpJF6vfnSr3uZZlxzEs'
    request_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    for i in range(len(location_words)):
        if i is not 0:
            request_url = request_url + '+'
        request_url = request_url + location_words[i]
    request_url = request_url + '&key=' + API_KEY
    r = requests.get(request_url)
    # print(r.text["results"]["geometry"]["location"])
    # print(r.text["results"])
    jsond = json.loads(r.text)
    lat = (jsond["results"][0]["geometry"]["location"]["lat"])
    lng = (jsond["results"][0]["geometry"]["location"]["lng"])
    print(('{0}, {1}').format(lat, lng))