import json
import re
import info
from entry import Entry

#index is the index of the word of the location

def findLocationFlag(convertedJson):
    loc = ""
    sal = 0
    haslocation = False
    for entity in convertedJson["entities"]:
        if entity["type"] == "LOCATION" and entity["name"] not in info.states:
            haslocation = True
            if entity["salience"] > sal:
                loc = entity["name"]
                sal = entity["salience"]
    # if not haslocation or sal <= .1:
    if not haslocation:
        return None
    return loc

def getIndex(l, target):
    for i in range(len(l)):
        if target in l[i]:
            return i
    return -1

def findInList(word_list, target):
    # print(word_list)
    # print(target)

    index = getIndex(word_list, target[0])
    length = len(target)

    for t in target:
        if not t in word_list[index:index + length]:
            return -1

    return index

def findLocation(body, locationFlag):

    body_split = re.split(r'[\'";,\s]\s*', body)

    words = []

    for word in body_split:
        if word != "":
            words.append(word.strip("#.!:()*\"\\/…"))

    cleaned_location_flags = []
    for flag in locationFlag.split():
        cleaned_location_flags.append(flag.strip("…#.*!()'\"\\/"))

    index = findInList(words, cleaned_location_flags)

    if index >= len(body) or index <= 0:
        return None

    cursor = index
    while cursor >= 0 and not words[cursor].isdigit():
        cursor -= 1

    if cursor < 0:
        return None

    return " ".join(words[cursor:index + len(cleaned_location_flags)])

def find_Loc(analyzed_tweet, original_tweet):
    convertedJson = dict()
    # with open("info.json") as f:
    #     convertedJson = json.load(f)
    convertedJson = json.loads(analyzed_tweet)
    # print(convertedJson)
    # convertedJson = json


    locationFlag = findLocationFlag(convertedJson)

    tweet = original_tweet
    # if locationFlag != None:
    #     print("determined location: " + findLocation(tweet, locationFlag))
    if locationFlag is not None:
        return findLocation(tweet,locationFlag)
    else:
        return None