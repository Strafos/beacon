from __future__ import absolute_import, print_function

import pprint
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from constants import *
import json
import time
import info

tweets = open('tweets3.txt', 'w')

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    stored_tweets = []
    def on_data(self, data):
        a = json.loads(data)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(a)
        try: 
            tweet = a["text"]
        except: 
            return True
        idx = 0
        if 'RT @' in tweet:
            idx = data.index(':') + 1
        if tweet not in self.stored_tweets and any(num in tweet for num in info.nums):
            if any(kw in tweet for kw in info.help_words):
                print(tweet)
                tweets.write(tweet + '\n')
                self.stored_tweets.append(tweet)
        # if tweet not in self.stored_tweets.values():
        #     for num in info.nums:
        #         if num in tweet:
        #             for kw in info.help_words:
        #                 if kw in tweet:
        #                     self.stored_tweets[tweet[:5]] = tweet
        #                     print(tweet)
        #                     # print(h)
        #                     # print(self.hashed_tweets)
        #                     # print(data)
        #                     tweets.write(tweet)
        #                     return True
        return True

    def on_error(self, status):
        print(status)
# 
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#Hurricaneirma', '#Irma', '#Irmarescue'])
