    print("Retrieving...")
    u_id=tweet.user.id
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
            hashtag_used.append(x1['text)
    else:
        has_hashtag=False
        hashtag_used="None"
    if tweet.entities.user_mentions != None:
        has_usermentioned=True
        for x2 in tweet.entities.user_mentions:
            user_mention.append(x2['name)
    else:
        has_usermentioned=False
        user_mention="None"

    if tweet.entities.urls != None:
        has_url=True
        for x3 in tweet.entities.urls:
            urls.append(x3['url)
    else:
        has_url=False
        urls="None"
    t_created_at=tweet.created_at
