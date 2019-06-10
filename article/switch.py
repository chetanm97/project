import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
from . import twappconfig2 as tw
import json
from . import craller as c


def pre_class():
    political=[]
    ht=[]
    t_w=[]

    auth = OAuthHandler(tw.ckey,tw.csecret)
    auth.set_access_token(tw.akey,tw.asecret)
    api = tweepy.API(auth,wait_on_rate_limit_notify=True)
    trends1 = api.trends_place(23424848)
    # print('top tweets aquired')

    # for ele in trends1:
    #     for el in ele['trends']:
    #         ht.append(el['name'])
    #print(ht)
    ht=['#modi','#RahulGandhi','#namoagain','#BJP','#Congress','#modioneagain','#Rahulforbehatarbharat']
    try:
        for hastag in ht:
            t_w=[]
            count=0
            count1=0
            count2=0
            if count1 <= 20:
                for tweet in tweepy.Cursor(api.search,q=hastag,rpp=100,result_type="recent",include_entities=True,lang="en").items(100):
                    t_w.append(tweet.text)
                try:
                    y=c.classify(t_w)
                except:
                    continue
                for pred1 in y:
                    if pred1 == 'POLITICS':
                        count2+=1
                    else:count+=1
                if count2 >= 8:
                    political.append(hastag)
                else:
                    pass
            count1+=1
    except Exception as e: print(e)

    finally:
        return political




    # print('tweets retrieved for '+hastag)
    # print('list of tweets returned')
    # print(political)
