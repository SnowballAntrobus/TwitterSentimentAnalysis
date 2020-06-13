import pandas as pd


def fix_mode(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    for (i, s) in df['Mode Sentiment'].iteritems():
        df.at[i, 'Mode Sentiment'] = s[5:]
    for (i, s) in df['Mode Fine Sentiment'].iteritems():
        df.at[i, 'Mode Fine Sentiment'] = s[5:]
    df.to_csv('descriptive_statistics_fix.csv')
