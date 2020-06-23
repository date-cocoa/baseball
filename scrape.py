from bs4 import BeautifulSoup
import requests
import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

HOME_URL = 'https://npb.jp/bis/yearly/'
LEAGUE = ['centralleague_', 'pacificleague_']

html_result = BeautifulSoup(requests.get(url).text).find_all('td','yearlyStats')
years = np.arange(1950, 2020, 1)

scores = []
for year in years:
    url = HOME_URL + LEAGUE[0] + str(year) + '.html'
    html_result = BeautifulSoup(requests.get(url).text).find_all('td','yearlyStats')
    number_of_games = int(html_result[0].text)
    score = 0


    for idx in [26, 35, 44, 53, 62, 71]:
        score += int(html_result[idx].text)
    
    score = score / number_of_games
    scores.append(score)
    time.sleep(3)

    print('finish' + str(year) + '!!')

central_data = pd.DataFrame(scores)
central_data.columns = ['score']
central_data.to_csv('./centralleague.csv')

# TO DO LEAGUE
scores = []
for year in years:
    url = HOME_URL + LEAGUE[1] + str(year) + '.html'
    html_result = BeautifulSoup(requests.get(url).text).find_all('td','yearlyStats')
    number_of_games = int(html_result[0].text)
    score = 0


    for idx in [26, 35, 44, 53, 62, 71]:
        score += int(html_result[idx].text)
    
    score = score / number_of_games
    scores.append(score)
    time.sleep(3)

    print('finish' + str(year) + '!!')

central_data = pd.DataFrame(scores)
central_data.columns = ['score']
central_data.to_csv('./pacificleague.csv')

df_central = pd.read_csv('./centralleague.csv')
df_pacific = pd.read_csv('./pacificleague.csv')

sns.set()
fig = plt.figure(figsize=(15, 7))
sns.lineplot(x=years, y=df_central['score'], label='central')
sns.lineplot(x=years, y=df_pacific['score'], label='pacfic')
fig.savefig('./plot.png')


