from utils import make_haiku_line

from secret import *

import emoji 
import tweepy

def make_haiku(): 
    tweet_text = ''.join(make_haiku_line(5)) + '\n' 
    tweet_text += ''.join(make_haiku_line(7)) + '\n' + ''.join(make_haiku_line(5))
    return tweet_text

def tweet(message): 
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	auth.secure = True
	print("Posting message {}".format(message))
	api.update_status(status=message)

tweet(make_haiku())
