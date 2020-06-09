import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def graph_scores(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    name = csv_file[:-4]

    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    sns.countplot(df['sentiment'], order=["Negative", "Neutral", "Positive"], ax=ax[0])
    sns.countplot(df["fine grain sentiment"], order=["Very Negative", "Slightly Negative",
                                                     "Neutral", "Slightly Positive", "Very Positive"], ax=ax[1])
    plt.savefig(name+'.png')


# test
# graph_scores('test1.csv')
# graph_scores('test2.csv')
