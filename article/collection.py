import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
from django.conf import settings
import pandas as pd
from .models import user_details,twitter_data,tweet_by_user,hash_id,user_mentioned,user_url,polarity
import json
import datetime
from . import twappconfig as tw
from . import tweet_crawler as tc
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
auth = OAuthHandler(tw.ckey,tw.csecret)
auth.set_access_token(tw.akey,tw.asecret)
api = tweepy.API(auth)



def abstraction(a):

    mtot=0
    for i in a:
        print(a[i])
        pos_bjp,pos_cong,neg_bjp,neg_cong,total=0,0,0,0,0
        stime=datetime.datetime.now()
        for tweet in tweepy.Cursor(api.search,q=i,result_type="recent",include_entities=True,lang="en").items(1000):
            tc.tweetr(tweet)
            score = analyser.polarity_scores(tweet.text)
            print(score['pos'],score['neg'])
            if score['pos'] > score['neg']:
                if a[i] =='BJP':
                    pos_bjp+=1
                elif a[i]=='Congress':
                    pos_cong+=1
            if score['neg'] > score['pos']:
                if a[i] =='BJP':
                    neg_bjp+=1
                elif a[i]=='Congress':
                    neg_cong+=1
            total+=1
        mtot+=total   
        etime=datetime.datetime.now()
        polarity(pos_bjp=pos_bjp,pos_cong=pos_cong,neg_bjp=neg_bjp,neg_cong=neg_cong,total=total,stime=stime,etime=etime).save()   
    
