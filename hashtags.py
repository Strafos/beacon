from __future__ import absolute_import, print_function

import pprint
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from constants import *
import json
import time

nums = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '6': '6',
    '7': '7',
    '5': '5',
    '8': '8',
    '9': '9',
}

help_words = ['help','!','family','stuck','trapped',]

tweets = open('tweets3.txt', 'w')

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        a = json.loads(data)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(a)
        tweet = a['text']
        idx = 0
        if 'RT @' in tweet:
            idx = data.index(':') + 1
        for num in nums.values():
            if num in tweet:
                for kw in help_words:
                    if kw in tweet: 
                        print(tweet)
                        tweets.write(tweet)
                        return True
        return False

    def on_error(self, status):
        print(status)
# 
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#Hurricaneirma', '#Irma', '#Irmarescue', '#SOSharvey', '#harveyrescue'])
