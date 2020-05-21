# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:45:20 2020

@author: Pranav Tumkur
"""

import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from textblob import TextBlob
from pandasql import sqldf
pysqldf= lambda q: sqldf(q, globals())
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import NMF


df_tweets=pd.read_pickle('..//SQL for data science/Cleaned_tweets_pickle.pkl')
df_merged=pd.read_pickle('..//SQL for data science/Merged_tweets+user_pickle.pkl')

df_tweettext= df_tweets.filter(['text'])
df_hashtags= df_tweets.filter(['Hashtag'])

dct_common_wrds={}
Stop_words=["The", "&", "-", "...","I","My","We","i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
df_stopwords= pd.DataFrame(Stop_words, columns=['Stop_words'])

'''FREQUENT WORDS USING DICTIONARY'''  
for x in df_tweettext['text']:
    wrd_lst=x.split()
    for word in wrd_lst:
        if word not in Stop_words:
            dct_common_wrds[word]=dct_common_wrds.get(word,0)+1
#for k,v in sorted(dct_common_wrds.items(), key=lambda item:item[1], reverse= True)[:20]:
#        print(k,v)

'''FREQUENT WORDS USING COUNTER FUNCTION'''           
#display(pysqldf("select * from df_tweettext"))
df_tweettext_wostpwords= df_tweettext.text.apply(lambda word: [word.lower() for word in word.split(' ') if word.lower() not in Stop_words])

dct_common_wrds={}
wrds_consolidated_nosw=[]
for wrd_lst in df_tweettext_wostpwords.iloc[:]:
    for word in wrd_lst:
        wrds_consolidated_nosw.append(word)
#dct_common_wrds=Counter(wrds_consolidated_nosw)     
#print([(k,v) for k,v in sorted(dct_common_wrds.items(), key=lambda item:item[1], reverse= True)][:20])

'''
def Count_instances_in_df(df_name, col_name):
    dct={}
    for x in df_name[col_name]:
        if type(x)==list:  #Forlists
            for y in x:
                y='#'+y.lower()
                dct[y]=dct.get(y,0)+1
    return(dct)

WORD CLOUD CREATION
def Make_wordcloud_for_freq(freq_dict):
    wordcloud= WordCloud().generate_from_frequencies(freq_dict)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
#Make_wordcloud_for_freq(dct_common_wrds)
Make_wordcloud_for_freq(Count_instances_in_df(df_hashtags,'Hashtag'))

SENTIMENT ANALYSIS
#df_tweettext_senti= df_tweettext.text.apply(lambda word: text
senti_list=[]
subj_list=[]
for text in df_merged['text']:
    senti_list.append(TextBlob(text).sentiment[0])
    subj_list.append(TextBlob(text).sentiment[1])

Using lambda instead of for loop
#df_merged['Sentiment']= df_merged.text.apply(lambda text: TextBlob(text).sentiment[0]) 
#df_merged['Subjectivity']= df_merged.text.apply(lambda text: TextBlob(text).sentiment[1]) 

df_merged['Sentiment']= senti_list
df_merged['Subjectivity']= subj_list

print(df_merged['Subjectivity'].mean())

df_usersentiments= df_merged.filter(['screen_name_x','text','retweet_count','Sentiment','Subjectivity'])
#display(pysqldf('select screen_name_x, sum(Sentiment), sum(retweet_count) from df_usersentiments group by screen_name_x order by sum(Sentiment) desc limit 30'))
#display(pysqldf('select Subjectivity,text from df_usersentiments order by Subjectivity limit 30'))
'''

df_tweettext_wostpwords['text']= df_tweettext.text.apply(lambda word: " ".join([word.lower() for word in word.split(' ') if word.lower() not in Stop_words]))

bow=CountVectorizer()
X= bow.fit_transform(df_tweettext_wostpwords.text)
#print(X)

index2word= np.array(bow.get_feature_names())
nmf= NMF(n_components=7, solver="mu")
W= nmf.fit_transform(X)
H= nmf.components_

for i, topic in enumerate(H):
    print('Topic Cluster {}: {}'.format(i+1, ",".join([str(term) for term in index2word[topic.argsort()[-15:]]])))






