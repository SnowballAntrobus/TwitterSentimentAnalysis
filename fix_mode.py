import pandas as pd


def score_numerical(pred):
    if pred == "Negative":
        pred = -1

    elif pred == "Neutral":
        pred = 0

    elif pred == "Positive":
        pred = 1
    return pred


def score_numerical_fine(pred):
    if pred == "Very Negative":
        pred = 1
    elif pred == "Slightly Negative":
        pred = 2
    elif pred == "Neutral":
        pred = 3
    elif pred == "Slightly Positive":
        pred = 4
    elif pred == "Very Positive":
        pred = 5
    return pred


def fix_mode(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    for (i, s) in df['Mode Sentiment'].iteritems():
        df.at[i, 'Mode Sentiment'] = score_numerical(s[5:])
    for (i, s) in df['Mode Fine Sentiment'].iteritems():
        df.at[i, 'Mode Fine Sentiment'] = score_numerical_fine(s[5:])
    df.to_csv('descriptive_statistics_fix.csv')


fix_mode('descriptive_statistics.csv')
