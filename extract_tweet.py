import json
import google_nlp
import info

file = open("tweets.txt", "r")
# output_tweets = open("just_tweets.txt", "w")
output_tweets = open("tweets_info_filtered.txt", "w")


stored_tweets = []
for tweet in file.readlines():
    tweet_formatted = json.loads(tweet)
    tweet_text = tweet_formatted["text"]
    if tweet_text not in stored_tweets and any(num in tweet for num in info.nums):
            if any(kw in tweet for kw in info.help_words):
                stored_tweets.append(tweet_text)
                output_tweets.write("(" + tweet_formatted["text"] + ", " + tweet_formatted["user"]["screen_name"] + ", "
                                + tweet_formatted["created_at"] + ") \n")
                google_nlp.enter_coord(tweet_text)
output_tweets.close()