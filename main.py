from driver import driver
import pandas as pd
from tqdm import tqdm
import time
import datetime

results = []

# dates = ['2019-10-31', '2019-11-15', '2019-11-30', '2019-12-15', '2019-12-31', '2020-01-15',
#        '2020-01-31', '2020-02-15', '2020-02-29', '2020-03-15',
#        '2020-03-31', '2020-04-15', '2020-04-30', '2020-05-15', '2020-05-31', '2020-06-09']
start = datetime.datetime(2019, 10, 31)
end = datetime.datetime(2020, 6, 9)
dates = pd.date_range(start, end, freq='D')
dates = dates.strftime('%Y-%m-%d').tolist()

for d in tqdm(range(len(dates) - 1)):
    if d % 10 == 0 and d != 0:
        time.sleep(600)
    results.append(driver(1000, dates[d], dates[d + 1], query='#coronavirus OR #coronavirusoutbreak OR '
                                                              '#coronavirusPandemic OR #covid19 OR #covid_19 OR '
                                                              '#epitwitter OR #ihavecorona OR #health OR #virus OR '
                                                              'coronavirus OR covid19 OR pandemic'))
    df = pd.DataFrame(results, columns=['Date Range', 'Average Sentiment',
                                        'Median Sentiment', 'Mode Sentiment',
                                        'STDev Sentiment', 'Average Fine Sentiment',
                                        'Median Fine Sentiment', 'Mode Fine Sentiment',
                                        'STDev Fine Sentiment', 'Number of Tweets'])

    df.to_csv('descriptive_statistics.csv')
