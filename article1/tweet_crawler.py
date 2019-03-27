import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
from django.conf import settings
#from django.db import transaction
import pandas as pd
from .models import user_details,twitter_data,tweet_by_user,hash_id,user_mentioned,user_url
import json
#from django.http import HttpResponse
from . import twappconfig as tw
auth = OAuthHandler(tw.ckey,tw.csecret)
auth.set_access_token(tw.akey,tw.asecret)
api = tweepy.API(auth)

def tweetr():
    for tweet in tweepy.Cursor(api.search,q="#modi",rpp=1,result_type="recent",include_entities=True,lang="en").items(10):
        t_text=tweet.text
        u_name=tweet.user.name
        u_location=tweet.user.location if tweet.user.location != None else "None"
        u_url=tweet.user.url if tweet.user.url != None else "None"
        u_description=tweet.user.description if tweet.user.description != None else "None"
        u_screenname=tweet.user.screen_name if tweet.user.screen_name != None else "None"
        followers_count=tweet.user.followers_count
        friends_count=tweet.user.friends_count
        status_count=tweet.user.statuses_count
        u_created_at=tweet.user.created_at
        t_id=tweet.id
        hashtag_used=[]
        user_mention=[]
        urls=[]
        reply_to_status=tweet.in_reply_to_status_id_str if tweet.in_reply_to_status_id_str != None else "None"
        reply_to_user_id=tweet.in_reply_to_status_id_str if tweet.in_reply_to_status_id_str != None else "None"
        u_id=tweet.text.id
        if tweet.place != None:
            ted_country=tweet.place.country
            ted_city=tweet.place.full_name
        else:
            ted_country="None"
            ted_city="None"
        retweet_count=tweet.retweet_count
        t_language=tweet.lang
        if tweet.entities.hashtags != None:
            has_hashtag=True
            for x1 in tweet.entities.hashtags:
                hashtag_used.append(x1.text)
        else:
            has_hashtag=False
            hashtag_used="None"
        if tweet.entities.user_mentions != None:
            has_usermentioned=True
            for x2 in tweet.entities.user_mentions:
                user_mention.append(x2.name)
        else:
            has_usermentioned=False
            user_mention="None"

        if tweet.entities.urls != None:
            has_url=True
            for x3 in tweet.entities.urls:
                urls.append(x3.url)
        else:
            has_url=False
            urls="None"
        t_created_at=tweet.created_at
        print("User ID is ",u_id)
        print("Tweet ID is ",t_id)
        print("Tweet is ",t_text)
        print("Creating DataFrames...")
        m.user_details(user_id=u_id,username=u_name,location=u_location,url=u_url,screenname=u_screenname,description=u_description,followers_count=followers_count,friends_count=friends_count,status_count=status_count,created_at=u_created_at).save()
        m.twitter_data(tweet_id=t_id,text=t_text,reply_to_status=reply_to_status,reply_to_user_id=reply_to_user_id,city=ted_city,country=ted_country,retweet_count=retweet_count,lang=t_language,hashtag=has_hashtag,user_mentioned=has_usermentioned,url=has_url,created_at=t_created_at).save()
        m.tweet_by_user(user_id=u_id,tweet_id=t_id).save()
        for x1 in hashtag_used:
            m.hash_id(tweet_id=t_id,hashtag=x1).save()
        for x2 in user_mention:
            m.user_mentioned(tweet_id=t_id,mentioned=x2).save()
        for x3 in urls:
            m.user_url(tweet_id=t_id,url=x3).save()
        print("To SQL Database...")
        print("\n\n\n\n\n")
