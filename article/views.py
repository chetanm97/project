from django.shortcuts import render, redirect
import os
from . import collection as c
from django.http import HttpResponse
from article.models import user_details,twitter_data,tweet_by_user,hash_id,user_mentioned,user_url
import sys 

def alist(request):
    return render(request, 'article/alist.html')

def output(request):
    
    return redirect('../hashlist/')

def stop(request):
    os.abort()
    # sys.exit()
    return redirect('article/alist.html')

