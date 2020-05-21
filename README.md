# Analysis of Twitter data for Lobbyists4America

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
