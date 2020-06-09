import csv
import tweepy
import GetOldTweets3 as got
import pandas as pd
import numpy as np


def get_tweet_replies(name, tweet_id, csv_name):
    # info from twitter dev account
    auth = tweepy.OAuthHandler('API Key', 'API Secret')
    auth.set_access_token('Access Token', 'Access Token Secret')

    api = tweepy.API(auth)

    replies = []
    for tweet in tweepy.Cursor(api.search, q='to:' + name, result_type='recent', timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == tweet_id:
                replies.append(tweet)

    with open(csv_name, 'wb') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
        csv_writer.writeheader()
        for tweet in replies:
            row = {'user': tweet.user.screen_name, 'text': tweet.text.encode('ascii', 'ignore').replace('\n', ' ')}
            csv_writer.writerow(row)


# since and until format is "2015-05-01"
def get_old_tweets(num, since, until, csv_name, name=None, query=None):
    tweet = None
    if name is not None:
        tweetCriteria = got.manager.TweetCriteria().setUsername(name).setSince(since).setUntil(until).setMaxTweets(num)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    elif query is not None:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setSince(since).setUntil(until) \
            .setMaxTweets(num)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    text_tweets = [[tw.username, tw.text] for tw in tweet]
    df = pd.DataFrame(text_tweets, columns=['user', 'text'])
    df['text'].replace('', np.nan, inplace=True)
    df.dropna(subset=['text'], inplace=True)
    df.to_csv(csv_name)


# tests
# get_old_tweets(10, "2020-06-07", "2020-06-08", "test1.csv", name='realDonaldTrump')
# get_old_tweets(10, "2020-06-07", "2020-06-08", "test2.csv", query='COVID')
