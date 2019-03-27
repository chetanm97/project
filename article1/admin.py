from django.contrib import admin
from .models import user_details,twitter_data,tweet_by_user,hash_id,user_mentioned,user_url
# Register your models here.



admin.site.register(user_details)
admin.site.register(twitter_data)
admin.site.register(tweet_by_user)
admin.site.register(hash_id)
admin.site.register(user_mentioned)
admin.site.register(user_url)