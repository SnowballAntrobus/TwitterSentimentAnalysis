import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transormer_score import transformer_score


def clean_tweet(tweet):
    clean = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return clean


def sentiment_scores_vader(texts):
    scores = []
    analyzer = SentimentIntensityAnalyzer()
    for text in texts:
        sentiment_dict = analyzer.polarity_scores(text)

        if sentiment_dict['compound'] >= 0.05:
            scores.append("Positive")

        elif sentiment_dict['compound'] <= - 0.05:
            scores.append("Negative")

        else:
            scores.append("Neutral")
    return scores


# 0-5 vneg-neg-nut-pos-vpos
def add_sentiment(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    texts = []
    for i in df.index:
        texts.append(clean_tweet(df['text'][i]))

    vader_scores = sentiment_scores_vader(texts)
    transformer_scores = transformer_score(texts)
    df["sentiment"] = vader_scores
    df["fine grain sentiment"] = transformer_scores

    df.to_csv(csv_file)


# test
# add_sentiment('test1.csv')
# add_sentiment('test2.csv')
