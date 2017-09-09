import json
import re

#index is the index of the word of the location

def findLocationFlag(convertedJson):
    loc = ""
    sal = 0
    haslocation = False
    for entity in convertedJson["entities"]:
        if entity["type"] == "LOCATION":
            haslocation = True
            if entity["salience"] > sal:
                loc = entity["name"]
                sal = entity["salience"]

    if not haslocation: return None
    return loc

def findInList(word_list, target):
    print(word_list)
    print(target)
    index = word_list.index(target[0])
    length = len(target)

    for t in target:
        if not t in word_list[index:index + length]:
            return -1

    return index


def findLocation(body, locationFlag):

    body_split = re.split(r'[;,\s]\s*', body)

    words = []

    for word in body_split:
        words.append(word.strip("#.!"))

    index = findInList(words, locationFlag.split())

    if index >= len(body) or index < 0:
        return
    elif index == 0:
        return words[index]

    cursor = index
    while cursor > 0 and not words[cursor].isdigit():
        cursor -= 1

    return " ".join(words[cursor:index + len(locationFlag.split())])

def find_Loc(analyzed_tweet, original_tweet):
    convertedJson = dict()
    # with open("info.json") as f:
    #     convertedJson = json.load(f)
    convertedJson = json.loads(analyzed_tweet)
    # convertedJson = json


    locationFlag = findLocationFlag(convertedJson)

    tweet = original_tweet
    # tweet = "Water rising quick please help ASAP please!!\n820 smith street, port Arthur Texas,77640"
    print("tweet: \n\t" + tweet)
    print()
    if locationFlag != None:
        print("determined location: \n\t" + findLocation(tweet, locationFlag))
    #now words[index] is a number, the 45 in 45 oak avenue mercer county