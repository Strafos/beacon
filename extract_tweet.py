import json

file = open("tweets.txt", "r")
output_tweets = open("just_tweets.txt", "w")

for tweet in file.read().splitlines():
    tweet_formatted = json.loads(tweet)
    output_tweets.write(tweet_formatted["text"] + "\n")

output_tweets.close()