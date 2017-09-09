import string

#index is the index of the word of the location

def parseLanguage(body, locationFlag):

    words = []

    for word in body.split():
        words.append(word.strip("#.!"))

    index = words.index(locationFlag)

    if index >= len(body) or index < 0:
        return
    elif index == 0:
        return words[index]

    cursor = index
    while cursor >= 0 and not words[cursor].isdigit():
        cursor -= 1

    return " ".join(words[cursor:index + 1])

print(parseLanguage("My 83 y.o. Parents in imminent danger at 4922 Loch Lomond #Meyerland. Water knee deep inside home. Mom=heart condition. Dad=Alzheimer's", "Meyerland"))
#now words[index] is a number, the 45 in 45 oak avenue mercer county

