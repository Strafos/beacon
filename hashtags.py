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
import google_nlp

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
                self.stored_tweets.append(tweet)
                google_nlp.enter_coord(tweet)
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