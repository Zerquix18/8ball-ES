#!/usr/bin/env python
'''
	Hey there

	Author: Zerquix18
'''

import random
import json
import sys
from tweepy.streaming import StreamListener
from tweepy           import OAuthHandler
from tweepy           import Stream
from tweepy           import API
#import love          # not found, sorry.

reload(sys)
sys.setdefaultencoding("utf-8")

# fire when the strob hits you:
consumer_key        = '3z6o751olyBNSvSj6g4RRow7Y'
consumer_secret     = '0SJM9D39WgGph0sFNQOlrlE0AiF98Qew36WoNe95ZftyRaWg76'
access_token        = '4307769972-msYmmG921lpJKCR8sf9MAQReGUFF1p7aELtuUtj'
access_token_secret = 'chqzNy3c1Kj1lQ7hMJCtLMsjI0kbh7cOs00C36t4IZcZg'

# bet you're looking for something neww ohoh oh (8)

possible_replies = open('possible_replies.txt').read(10000).split("\n")

# this thing receives it all
class StdOutListener(StreamListener):
    # gets the data
    def on_data(self, data):
        data         = json.loads(data)
        text         = data['text']
        print 'Received: ' + text
        # it has to be a mention and end with a question mark
        if "?" not in text:
            print 'not a question...'
            return
        # ok now let's reply
        content  = random.choice(possible_replies)
        user     = data['user']['screen_name']
        tweet_id = data['id']
        tweet    = '@' + user + ' ' + content

        api.update_status(tweet, tweet_id)
        print 'Replied: ' + tweet

        return True

    def on_error(self, status):
        pass

if __name__ == '__main__':

    ## class that will get everything    
    l      = StdOutListener()
    ## start the connection
    auth   = OAuthHandler(consumer_key, consumer_secret)
    ## add access tokens
    auth.set_access_token(access_token, access_token_secret)
    ## link connection to the class
    stream = Stream(auth, l)
    ## connect to the rest API
    api    = API(auth)

    print 'starting:'
    stream.filter(track=['@8ball_es'])
