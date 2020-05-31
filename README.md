# Analysis of Twitter data for Lobbyists4America
![Screenshot (230)](https://user-images.githubusercontent.com/65482013/83346603-88199f80-a33b-11ea-89f2-202c73779aab.jpg)(https://www.lobbyists4good.org/)

## The Interest
Having an avid interest in American politics and also intrigued by the unique concept of lobbying for a bill, this particular dataset appealed to me.
Boots-on-the-ground lobbying is the best way to influence legislation in D.C., but everyday people do not have the same access to lobbyists as large corporations and wealthy special interest groups.
To address this, [Lobbyists_4_Good](https://www.lobbyists4good.org/) proposes a unique concept- campaigns started by individuals raising money to lobby for causes important to the people.

## The Data
The dataset was publically available in the form of all tweets related to the cause of Lobbyists4Good were available [here](https://www.dropbox.com/sh/qrq1pcjsji0v03u/AAC639WcH58tM0YZperwY388a?dl=0)

## The Test Case
The following was the test case assumed by me : _Lobbyists4Good is a company that seeks to provide insights to their customers (who aim to affect legislation within the US). They want an analysis of the 2008-2017 congressional tweets in order to understand key topics, members, and relationships within Congress. These insights will help them focus and strengthen their lobbying efforts._

## Data Collection

The tweets were available in a huge **(1.6GB)** json file. All tweet parameters were in separate dictionaries, separated by a ‘\n’. But, Python does not parse multiple dictionaries using the inbuilt json functions.
Separating these dictionaries according to ‘\n’, I tried to make a list of all these dictionaries, which I could then parse into a pandas df. But the problem with the json was its size. Such a large json could not be handled by Python and it showed a memory error.
I therefore had to ‘pickle’ the pandas dataframe object into local memory using Anaconda-Spyder. I gave overnight runs to collect all data into the df, using [this](https://github.com/pranavtumkur/Lobbyists4America-tweets-and-users/blob/master/Making%20df%20from%20tweets_json.py) code.

It took around 15mins to fetch and store 10k records and longer as I went deeper into the data. Another problem was, some rows has a list as its value, i.e the ‘key’ in the original dictionary has a list of dictionaries as its ‘value’! I found a way to fetch these buried values and add them to the df column.
The json file could not be opened (notepad says the file is too large, Google Chrome crashes and no online json editor takes that big a file), so I had to kept writing to a .csv file at every step to check how the data looked.

## Initial Exploration of Data and Project Proposal

Having cleaned the data, I was interested in finding some basic/prima-facie trends, counts and relations in the data. To begin with, I explored, the number of tweets by each Congressman, the people he mentions, the number of retweets, the popular hashtags, the time-based trends etc. I also prepared an initial [Entity-Relationship diagram](https://github.com/pranavtumkur/Lobbyists4America-tweets-and-users/blob/master/ER%20diagram.pdf).
Finally, taking into considering my knowledge on the subject and the EDA, I prepared a [project proposal](https://github.com/pranavtumkur/Lobbyists4America-tweets-and-users/blob/master/Developing%20a%20Project%20Proposal.docx) including the initial hypthoesis, the proposed approach, the metrics to be verified and the underlying assumptions (which would later need to be verified).

## Data Exploration

I found out trends, outliers, key parameters and performance indices using the user mentions, count of retweets, the popular hashtags, states which were most involved with the cause. I also tried to find out if there were any specific months in which the Congressmen were active (My initial hypothesis was- it would be the pre-election months). These observations were then compared to my initial hypothesis and the ERD was revised accordingly. This document is available [here](https://github.com/pranavtumkur/Lobbyists4America-tweets-and-users/blob/master/Descriptive%20Statistics%20and%20comparison%20with%20the%20initial%20hypothesis.docx) and the code used, is available [here](https://github.com/pranavtumkur/Lobbyists4America-tweets-and-users/blob/master/Exploration%20of%20data.py)

## Tweet text analysis
### *The most interesting part of the project was the analysis of actual tweet data!*

I did a textual analysis for Term Frequency. I tried to see which words were most frequently used in the tweets by the Congressmen in the context of Lobbyists4America, using a word cloud. The same was done for the commonly used hashtags too. Stop words were eliminated when analysing the same. This was followed by a sentiment and subjectivity analysis of the tweet data.

A correlation was found between the retweet count and the sentiment analysis. People who had a positive sentiment were more active and retweeted on the cause far more. A real shocker was the subjectivity analysis, which is heavily skewed towards 0 **(Avg.:0.292)**, suggesting that almost all tweets are just factual which should not be the case for such a humanitarian cause. On taking some sample data, it was found that the tweets were in fact related to the cause of Lobbyists4Good but since the same was explicitly not mentioned, keyword search failed to show the correct subjectivity score in these cases.

## The Conclusion

All trends indicate a growing interest in both the general public and the Congressmen for the causes projected by Lobbyists4Good, the focal point of interest being <ins>'Reduced Animal Agriculture'</ins>. All Congressmen's tweets display high a positivity score, showing that they actually care for the cause and support it whole-heartedly. This means good news for the CEO of Lobbyists4Good!
