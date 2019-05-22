# Trending Forecasting System on Twitter

## How to execute
To execute this tool, follow the next steps.

1 - Create a virtual environment and install as dependencies mentioned in the requirements.txt. Consider the command **pip install -r requirements.txt**.

2 - After activating the virtual environment clone the repository and in the file **tweets / api_twitter / src / initialize_api.py** fill in the tokens and keys fields of the twitter API. You will get these keys by signing up as a developer on Twitter.

2 - Open a terminal/command prompt in the main folder where the manage.py file is located and run the command: **python3 manage.py runserver**

3 - Open another terminal in the web folder. First of all it is necessary to run the command **npm update** to update the dependencies of the node, which were not included in the repository. Then run the command **ng serve --open**.

## How to use tool
To start, in the home tab, inform a topic of your interest and the amount of tweets you want to analyze. For practical purposes I recommend that you inform a known topic such as Game of Thrones, Avengers, Endgame, Donald Trump, etc. and a tweets amount over 100.

Another flap contains world trending topics. Here is a list of 10 trending topics from the time the survey was conducted. You can also use a trending topic to do the search on home.

The location tab contains the location of the users who made the tweets. Note that there are not the same amount of locations and tweets. This is because not all users report their locations. Even if they report, some users are from the same location, which will not generate different points on the map.

Finally, the results tab contains the information obtained after the API request. There are 3 charts, the first in a donut format, which represents the analysis of feelings classified into groups. The second and third are graphs of words that express good and bad feelings exhibiting the occurrence of words.
Note: Sometimes the word chart may return empty. This means that few tweets have been analyzed on the topic.

Finally, there is a list of the 5 best and 5 worst tweets obtained in the classification of feelings.

## Tool purpose

The proposal of the tool is to extract statistical results on products or topics of interest. The tool performs data cleaning and data mining operations. Their results are presented so that companies / individuals can make smart marketing decisions by looking at which products or topics are worth investing in and which locations to invest in.

## Tool WorkFlow

For the searched topic, tweets are requested from the twitter API. It returns various information for each tweet, such as the user, location, the tweet itself, etc. Once the tweet is received, it will undergo a sentiment analysis using the TextBlob library, which will classify it with a score between -1 and 1. Now the data cleanups start using regex and NLTK. The first cleanup removes emoji, links and anything that is unnecessary for analysis. After that, a tokenization of the tweets occurs. After the tokens are generated, a new cleaning is done, to remove stop words. Finally, there is a count of occurrences based on a base of English words that represent good and bad feelings. The charts are plotted by matplotlib and sent to the web page.

Trending topics are obtained through the twitter API that only returns us the topics in high, a list with approximately 50 topics. For presentation purposes only the top 10 are displayed.

Locations are extracted from home twitter. Initially they are supplied in the form of text, specifying the city. Sometimes this information is dirty, containing random text. These texts are filtered and compared using the regex engine. Obtained the locations the map is generated based on the Leaflet library.
