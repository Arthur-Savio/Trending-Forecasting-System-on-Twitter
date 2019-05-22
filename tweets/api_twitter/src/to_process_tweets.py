import re
import csv
import string
from textblob import TextBlob
from nltk.corpus import stopwords
from tweets.api_twitter.src.post_process import PostProcessTweets
from tweets.api_twitter.src.mining_location import MiningLocation

class ProcessTweets:
    #Class of processing and cleaning of data

    def __init__(self):
        self.emoticons_str = r"""
            (?:
                [:=;] # Eyes
                [oO\-]? # Nose (optional)
                [D\)\]\(\]/\\OpP] # Mouth
            )"""
        self.regex_str = [
            self.emoticons_str,
            r'<[^>]+>', # HTML tags
            r'(?:@[\w_]+)', # @-mentions
            r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
            r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
            r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
            r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
            r'(?:[\w_]+)', # other words
            r'(?:\S)' # anything else
        ]
        self.tokens_re = re.compile(r'('+'|'.join(self.regex_str)+')', re.VERBOSE | re.IGNORECASE)
        self.emoticon_re = re.compile(r'^'+self.emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
        self.stop = list()
        self.tokens = list()
        self.terms_only = list()
        self.bad_words = list()
        self.good_words = list()
        self.count_bad = dict()
        self.count_good = dict()
        self.good_words = list()
        self.bad_words = list()
        self.all_tweets = list()
        self.selected_tweets = list()
        self.user_location = list()
        self.geo_location = list()
        self.tweets_with_score = dict()
        self.sentiment_datas = [0 for i in range(0, 3)]

    def initialize_process(self):
        self.read_datas_to_generate_tokens()
        self.calculate_sentiment()
        self.update_selected_tweets()
        self.generate_stop_words()
        self.generate_clean_tokens()
        self.read_bad_and_good_words()
        self.count_commom_datas()
        PostProcessTweets(self.count_good, self.count_bad, self.sentiment_datas).generate_all_graphics()

    def read_datas_to_generate_tokens(self):
        with open('tweets/api_twitter/datas/tweets.csv', 'r') as file:
            my_csv = csv.reader(file)

            for line in my_csv:
                self.all_tweets.append(line[0])
                self.user_location.append(line[1])
                token = self.pre_process(line[0])
                for term in token:
                    self.tokens.append(term)

        self.geo_location = MiningLocation(self.user_location).treat_user_location()

    def pre_process(self, my_string, lowercase=False):
        #First data cleansing to take emojis and tokenize the tweets

        tokens = self.tokenize(my_string)
        if lowercase:
            tokens = [token if self.emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens

    def tokenize(self, s):
        return self.tokens_re.findall(s)

    def calculate_sentiment(self):
        #For each tweet the feelings expressed are analyzed by Textblob. Scores range from -1 to 1
        twittes_score = list()

        for i in self.all_tweets:
            analysis = TextBlob(str(i))
            polarity = analysis.sentiment.polarity
            twittes_score.append(polarity)
            self.tweets_with_score[polarity] = i

        for j in twittes_score:
            if j < -0.25:
                self.sentiment_datas[0] += 1
            elif -0.25 <= j <= 0.25:
                self.sentiment_datas[1] += 1
            else:
                self.sentiment_datas[2] += 1

    def generate_stop_words(self):
        self.stop = stopwords.words('english') + list(string.punctuation) + ['rt', 'RT', 'via', 'I', '...', '…', '’', '\n']

    def generate_clean_tokens(self):
        #Second data cleansing where the #, @, and stop words are removed
        
        self.terms_only = [term for term in self.tokens if term not in self.stop and not term.startswith(('#', '@'))]

    def update_selected_tweets(self):
        #Selecting the most important tweets. The most positive and the most negative.
        aux = sorted(self.tweets_with_score, reverse=True)

        count = 1
        for i in aux:
            if count < 5:
                self.selected_tweets.append(self.tweets_with_score[i])
            if count >= len(aux) - 5:
                self.selected_tweets.append(self.tweets_with_score[i])
            count += 1    

    def read_bad_and_good_words(self):
        with open('tweets/api_twitter/datas/synonym_good_words.txt', 'r') as f:
            self.good_words.append(f.readline().replace('\n', ''))
            while f.readline():
                self.good_words.append(f.readline().replace('\n', ''))

        with open('tweets/api_twitter/datas/synonym_bad_words.txt', 'r') as f:
            self.bad_words.append(f.readline().replace('\n', ''))
            while f.readline():
                self.bad_words.append(f.readline().replace('\n', ''))

    def count_commom_datas(self):
        #Count the most common words that express good and bad feelings.

        gw = set(self.good_words)
        bw = set(self.bad_words)

        for i in self.terms_only:
            if i in gw:
                if self.count_good.get(i) is None:
                    self.count_good[i] = 1
                else:
                    self.count_good[i] += 1
            if i in bw:
                if self.count_bad.get(i) is None:
                    self.count_bad[i] = 1
                else:
                    self.count_bad[i] += 1              
