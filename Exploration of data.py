# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:07:43 2020

@author: Pranav Tumkur
"""

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from IPython.display import display
from pandasql import sqldf
pysqldf= lambda q: sqldf(q, globals())

df_tweets=pd.read_pickle('..//SQL for data science/Cleaned_tweets_pickle.pkl')
df_merged=pd.read_pickle('..//SQL for data science/Merged_tweets+user_pickle.pkl')
#print(df.shape)

def Count_instances_in_df(df_name, col_name):
    dct={}
    for x in df_name[col_name]:
        if type(x)==list:  #Forlists
            for y in x:
                y=y.lower()
                dct[y]=dct.get(y,0)+1
        else:               #Forstrings
            if x is not None: x=x.lower()
            dct[x]=dct.get(x,0)+1   
    for k,v in sorted(dct.items(), key=lambda item:item[1]):
        print(k,v)

#Count_instances_in_df('Hashtag')
#Count_instances_in_df('Mentioned_user_name')
#Count_instances_in_df('in_reply_to_screen_name')
#Count_instances_in_df('lang')
#Count_instances_in_df(df_tweets,'screen_name')
#Count_instances_in_df(df_merged,'location')


df_retweets_freq_year= df_tweets.filter(['Date_parsed','retweet_count'], axis=1)
df_retweets_freq_month= df_tweets.filter(['Date_parsed','retweet_count'], axis=1)

 
df_retweets_freq_year['Date_parsed']=pd.to_datetime(df_retweets_freq_year['Date_parsed'])
df_retweets_freq_month['Date_parsed']=pd.DatetimeIndex(df_retweets_freq_month['Date_parsed']).month
#print(df_retweets_freq_month.describe())
#print(df_retweets_freq.cnt.mean()) # to find mean
#print(df_retweets_freq_month.std(axis = 0)) # to find std dev
#print(df_retweets_freq_month.head(10))
#print(df_retweets_freq.info())

#display(pysqldf("SELECT * FROM df_retweets_freq where retweet_count!=0 order by retweet_count desc"))

#df_retweets_freq_year.plot('Date_parsed','retweet_count')
#df_retweets_freq_year.Date_parsed.hist()
#df_retweets_freq_month.Date_parsed.hist()

#plt.plot(list(df['Date_parsed']),list(df['retweet_count']))
#plt.show()
