from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


def word_cloud(csv_file):
    df = pd.read_csv(csv_file)

    comment_words = ''
    stopwords = set(STOPWORDS)

    # iterate through the csv file
    for val in df.text:

        # typecaste each val to string
        val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        comment_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)

    # plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    name = csv_file[:-4]
    plt.savefig(name+"_wc.png")


# test
# word_cloud('test1.csv')
# word_cloud('test2.csv')
