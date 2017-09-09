import json

file = open("tweets1.txt", "r")
# output_tweets = open("just_tweets.txt", "w")
output_tweets = open("tweets_info.txt", "w")


for tweet in file.readlines():
    print(tweet)
    tweet_formatted = json.loads(tweet)
    output_tweets.write("(" + tweet_formatted["text"] + ", " + tweet_formatted["user"]["screen_name"] + ", "
                        + tweet_formatted["created_at"] + ") \n")

output_tweets.close()