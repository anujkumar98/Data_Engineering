import tweepy
import pandas as pd
import json
#from datatime import datatime
import s3fs
from dotenv import load_dotenv
import os

'''
def configure():
    load_dotenv()
'''
load_dotenv()

#Twitter authentication
access_key=os.getenv('access_key')
access_secret=os.getenv('access_secret')
consumer_key=os.getenv('consumer_key')
consumer_secret=os.getenv('consumer_secret')
auth=tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#Creating an API object
api=tweepy.API(auth)

tweeets=api.user_timeline(screen_name='@elonmusk',
                        count=200,
                        include_rts=False,
                        tweet_mode='extended'
                        )
print(tweeets)