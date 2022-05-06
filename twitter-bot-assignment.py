import tweepy

api_key = "Y4rwzfaembgiW3LhBco0SldVk"
api_key_secret = "8P794lsMVTltbgK3K2xJ4uZJIpohAwoPFRfDaxgIEyeEZF4HKC"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP%2FGaQEAAAAACVn03iqSsVzGlu8UHchcDU1aPLE%3Du6VFl4qo4kQbWJgiJyFyqqndpSdCPDz4Ar9SoPuy4aVjL2PXUB"
access_token_secret = "opCr3asJM8ssNCWYRg6PSFJNZIrBleei6IDS5TGVTvm9P"
access_token = "1505604838910009348-27CqzHepgtOCj2ZFxG87pegOD7jWwi"

#initialize a new tweepy instance
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret, wait_on_rate_limit=True)
username = "CHAfrica_tech"


def followUser(username):

    try:
        user = client.get_user(username=username).data
        client.follow_user(target_user_id=user.id)
    except:
        return 'request could not be completed'

def getUserTweets(username):
    try:
        user=client.get_user(username=username)
        return client.get_users_tweets(id=user[0].id, max_results=100).data
    except:
        return 'request could not be completed'

def retweet(tweet_id):
    client.retweet(tweet_id=tweet_id)

user_tweets_list = getUserTweets(username)
print(user_tweets_list)
i = 0
for j in user_tweets_list:
    id = user_tweets_list[i].data
    print(type(id))
    tweet_id = id.get('id')
    retweet(tweet_id)
    i += 1


"""
print(tweet_id)
tweets = user_tweets_list[1].data
print(type(tweets))
tweets_text = tweets.get('text')
print(tweets_text)

def unFollowUser(username):
    user=client.get_user(username=username)
    client.unfollow_user(target_user_id=user[0].id)

def getUsersFollowers(username):
    user=client.get_user(username=username)
    return client.get_users_followers(id=user[0].id, max_results=10).data

def getUsersFollowing(username):
    user=client.get_user(username=username)
    return client.get_users_following(id=user[0].id, max_results=10).data

def searchRecentTweets(query):
    return client.search_recent_tweets(query).data



def tweet(text):
    client.create_tweet(text=text)

def likeTweet(tweet_id):
    client.like(tweet_id=tweet_id)



def getLikedTweets(username):
user=client.get_user(username=username) """
# return client.get_liked_tweets(id=user[0].id, max_results=10).data
