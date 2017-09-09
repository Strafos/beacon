import json

file = open('tweets.txt', 'r')
for i in file.readlines():
    # print(i)
    a = json.loads(i)
    print(a["user"])
    break