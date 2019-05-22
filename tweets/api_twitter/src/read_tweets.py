import json
import csv
from tweepy.streaming import StreamListener


class MyListener(StreamListener):
    #Class that makes requests in the twitter API

    def __init__(self, term_to_search, limit):
        super().__init__()
        self.counter = 0
        self.limit = limit
        self.term_to_search = term_to_search
        self.datas = list()
        self.my_csv = None

    def on_data(self, data):
        #Read tweet by tweet and store in csv file for later review.
        #The reading ends when the data limit is received.

        try:
            result = dict()
            all_data = json.loads(data)

            result["text"] = all_data["text"]
            result["location"] = all_data["user"]["location"]

            if result["location"] is None:
                result["location"] = ''

            self.datas.append(result.copy())
            result.clear()

            self.counter += 1
            print(self.counter)

            if self.counter >= self.limit:
                with open('tweets/api_twitter/datas/tweets.csv', 'w') as file:
                    self.my_csv = csv.DictWriter(file, fieldnames=['text', 'location'])
                    self.my_csv.writeheader()
                    self.my_csv.writerows(self.datas)
                return False

        except BaseException as e:
            print("Error on_data: %s" % str(e))

    def on_error(self, status):
        return True
