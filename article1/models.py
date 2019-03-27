from django.db import models

# Create your models here.

class user_details(models.Model):
    user_id=models.CharField(max_length=256)
    username=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    url=models.CharField(max_length=256)
    screenname=models.CharField(max_length=256)
    description=models.CharField(max_length=1024)
    followers_count=models.IntegerField()
    friends_count=models.IntegerField()
    status_count=models.IntegerField()
    created_at=models.CharField(max_length=256)
    
class twitter_data(models.Model):
    tweet_id=models.CharField(max_length=256)
    text=models.CharField(max_length=1024)
    reply_to_status=models.CharField(max_length=256)
    reply_to_user_id=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    country=models.CharField(max_length=256)
    retweet_count=models.IntegerField()
    lang=models.CharField(max_length=256)
    hashtag=models.BooleanField(default=False)
    user_mentioned=models.BooleanField(default=False)
    url=models.BooleanField(default=False)
    created_at=models.CharField(max_length=256)
    
    
class tweet_by_user(models.Model):
    user_id=models.CharField(max_length=256)
    tweet_id=models.CharField(max_length=256)
    
class hash_id(models.Model):
    tweet_id=models.CharField(max_length=256)
    hashtag=models.CharField(max_length=256,default="None")
    
class user_mentioned(models.Model):
    tweet_id=models.CharField(max_length=256)
    mentioned=models.CharField(max_length=256,default="None")

class user_url(models.Model):
    tweet_id=models.CharField(max_length=256)
    url=models.CharField(max_length=256,default="None") 


