# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:13:59 2020

@author: Pranav Tumkur
"""

import datetime
import pandas as pd
import _pickle as pickle
import math

df_tweets=pd.read_pickle('..//SQL for data science/tweets_pickle.pkl')
df_users=pd.read_pickle('..//SQL for data science/users_pickle.pkl')


print(df_tweets.shape)
#print(df)

def Extract_into_newcol(df_name, og_col, new_col):
    lst=sublst=[]
    user_ment_col = df_name[og_col]
    for x in user_ment_col:
        if x==[] or type(x)==float or new_col not in x[0]:
            lst.append('')
        else:
            sublst=[]
            for y in x:
                sublst.append(y[new_col])
            lst.append((sublst))
            #print(lst)
    return(lst)

def Extract_counts(df_name, og_col, new_col):
    lst=sublst=[]
    user_ment_col = df_name[og_col]
    for x in user_ment_col:
        if x==[]:
            lst.append(0)
        else:
            sublst=[]
            for y in x:
                sublst.append(y[new_col])
            lst.append(len(sublst))
    return(lst)

c=0
date_lst=[]
m=7
multiplier=0
y=2008
while y<2012:
    if m<12:
        m+=1
    else:
        m=1
        y+=1
    multiplier+=1
    c+=12+4*multiplier
    for i in range(c):
        date = datetime.date(y,m,1)
        date_lst.append(date)
df_tweets['Date_parsed']=date_lst[:df_tweets.shape[0]]
print(len(date_lst))
      
df_tweets['Mentioned_user_name'] = Extract_into_newcol(df_tweets,'entities.user_mentions','screen_name')
df_tweets['Mentioned_user_id'] = Extract_into_newcol(df_tweets,'entities.user_mentions','id')
df_tweets['No_of_mentions'] = Extract_counts(df_tweets,'entities.user_mentions','id')
df_tweets['Hashtag'] = Extract_into_newcol(df_tweets,'entities.hashtags','text')
df_users['Official_URL'] = Extract_into_newcol(df_users,'entities.url.urls','display_url')

df_merged = pd.merge(df_tweets, df_users, left_on='user_id', right_on='id')
df_merged.to_csv('Tweets+User_merged.csv')


#print(df_tweets.head(25))
df_tweets.to_csv('Tweets_json.csv')
df_users.to_csv('Users_json.csv')

df_tweets.to_pickle('../SQL for data science/Cleaned_tweets_pickle.pkl') 
df_users.to_pickle('../SQL for data science/Cleaned_users_pickle.pkl') 
df_merged.to_pickle('../SQL for data science/Merged_tweets+user_pickle.pkl') 

#df = df.drop(df.columns[:], axis=1)


