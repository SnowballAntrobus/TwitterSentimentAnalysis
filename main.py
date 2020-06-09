from get_tweet import get_old_tweets
from analyze_tweet import add_sentiment
from word_cloud import word_cloud
from graph_scores import graph_scores


def main(num, since, until, name=None, query=None):
    csv_name = None
    if name is not None:
        csv_name = name + '_' + since + '_' + until + '.csv'
        get_old_tweets(num, since, until, csv_name, name=name)
    elif query is not None:
        csv_name = query + '_' + since + '_' + until + '.csv'
        get_old_tweets(num, since, until, csv_name, query=query)

    add_sentiment(csv_name)

    word_cloud(csv_name)

    graph_scores(csv_name)


main(10000, '2019-06-04', '2020-06-08', name='realDonaldTrump')
