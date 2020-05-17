# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:05:02 2020

@author: Pranav Tumkur
"""

import os.path
import json
import pandas as pd
from pandas.io.json import json_normalize
import _pickle as pickle

filename='../SQL for data science/Capstone/US_PoliticalTweets/US_PoliticalTweets/tweets.json'

fh=open(filename)
data = fh.read()

#fh1=open(filename1)
#data1 = fh1.read()
#print(data1[:100000000])
lst=lst1=[]
x=start_from=0
temp_dct=temp_dct1={}
df=None

rows_to_extract=1000
 
if os.path.exists('../SQL for data science/tweets_pickle.pkl'):
    df=pd.read_pickle('../SQL for data science/tweets.pkl')
    initial_rows=int(df.shape[0])
    for iterable in range(initial_rows):
        start_from=data.find('\n',start_from+1)
    for c in range(rows_to_extract):
        y=data.find('\n',start_from+1)
        if y>-1:
            #print(start_from,y)
            temp_js=json.loads(data[start_from:y])
            df_i=pd.json_normalize(temp_js)
            df=pd.concat([df,df_i])
        else:break
        start_from=y
    df.to_pickle('../SQL for data science/tweets_pickle.pkl')
else:
    for c in range(rows_to_extract):
        y=data.find('\n',start_from+1)
        if y>-1:
            #print(start_from,y)
            temp_js=json.loads(data[start_from:y])
            df_i=pd.json_normalize(temp_js)
            df=pd.concat([df,df_i])
        else:break
        start_from=y
    df.to_pickle('../SQL for data science/tweets_pickle.pkl')    
print(df)

'''print(y)

clean_jsonu=(json.loads(json.dumps(lst)))
clean_jsont=(json.loads(json.dumps(lst1)))

#print(clean_json)

dfu=pd.json_normalize(clean_jsonu)
dft=pd.json_normalize(clean_jsont)

#df['created_at']=pd.to_datetime(df['created_at'])
#pd.set_option('display.max_colwidth', None)
dfu.to_csv('Users_json.csv')
dft.to_csv('Tweets_json.csv')
#print(df.head(25))'''



