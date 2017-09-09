import nltk
import json

tweet = "Water rising quick please help ASAP please!!\n820 smith street, port Arthur Texas,77640"
tokens = nltk.word_tokenize(tweet)
print(tokens)   

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

with open("info.json") as f:
    convertedJson = json.load(f)

