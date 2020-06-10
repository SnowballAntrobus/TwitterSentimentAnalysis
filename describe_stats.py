import pandas as pd


def describe_stats(csv_file, since, until):
    df = pd.read_csv(csv_file, index_col=0)

    mode_sen = df['sentiment'].mode().to_string()
    mode_f_sen = df['fine grain sentiment'].mode().to_string()

    sen_ratings = {'Negative': -1, 'Neutral': 0, 'Positive': 1}
    f_sen_ratings = {"Very Negative": 1, "Slightly Negative": 2,
                     "Neutral": 3, "Slightly Positive": 4, "Very Positive": 5}

    df['sentiment'] = [sen_ratings[item] for item in df['sentiment']]
    df['fine grain sentiment'] = [f_sen_ratings[item] for item in df['fine grain sentiment']]

    avg_sen = df['sentiment'].mean()
    avg_f_sen = df['fine grain sentiment'].mean()

    med_sen = df['sentiment'].median()
    med_f_sen = df['fine grain sentiment'].median()

    std_sen = df['sentiment'].std()
    std_f_sen = df['fine grain sentiment'].std()

    num = len(df.index)

    return [since + ':' + until,
            avg_sen, med_sen,
            mode_sen, std_sen,
            avg_f_sen, med_f_sen,
            mode_f_sen, std_f_sen, num]
