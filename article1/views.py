from django.shortcuts import render
import os
from . import tweet_crawler as t
from django.http import HttpResponse
from article.models import user_details,twitter_data,tweet_by_user,hash_id,user_mentioned,user_url
import sys 

def alist(request):
    return render(request, 'article/alist.html')

def output(request):
    t.tweetr()
    return render(request,'article/alist.html')

def stop(request):
    t.tweetr().listener.stop()
    return render(request,'article/alist.html')

