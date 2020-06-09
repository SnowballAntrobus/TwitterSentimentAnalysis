from driver import driver
import pandas as pd

results = []
date = ['2019-12-31', '2020-01-15', '2020-01-31', '2020-02-15', '2020-02-29', '2020-03-15',
        '2020-03-31', '2020-04-15', '2020-04-30', '2020-05-15', '2020-05-31', '2020-06-09']
for d in range(len(date) - 1):
    results.append(driver(1000, date[d], date[d + 1], query='#coronavirus OR #coronavirusoutbreak OR '
                                                          '#coronavirusPandemic OR #covid19 OR #covid_19 OR '
                                                          '#epitwitter OR #ihavecorona OR #health OR #virus OR '
                                                          'coronavirus OR covid19 OR pandemic'))

df = pd.DataFrame(results, columns=['Date Range', 'Average Sentiment',
                                    'Median Sentiment', 'Mode Sentiment',
                                    'STDev Sentiment', 'Average Fine Sentiment',
                                    'Median Fine Sentiment', 'Mode Fine Sentiment',
                                    'STDev Fine Sentiment'])

df.to_csv('descriptive_statistics.csv')
