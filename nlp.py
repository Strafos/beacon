import json
import re

#index is the index of the word of the location

def findLocationFlag(convertedJson):
    loc = ""
    sal = 0
    for entity in convertedJson["entities"]:
        if entity["type"] == "LOCATION":
            if entity["salience"] > sal:
                loc = entity["name"]
                sal = entity["salience"]
    return loc

def findInList(list, target):
    print(list)
    print(target)
    index = list.index(target[0])
    length = len(target)

    for t in target:
        if not t in list[index:index + length]:
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

convertedJson = dict()
with open("info.json") as f:
    convertedJson = json.load(f)

locationFlag = findLocationFlag(convertedJson)

tweet = "Water rising quick please help ASAP please!!\n820 smith street, port Arthur Texas,77640"
print("tweet: \n\t" + tweet)
print()
print("determined location: \n\t" + findLocation(tweet, locationFlag))
#now words[index] is a number, the 45 in 45 oak avenue mercer county

