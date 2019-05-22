import json

class ReadTrendingTopics:
    #Twitter API request trending topics

    def __init__(self, api):
        self.api = api
        self.trends = None
        self.trends_list = list()

    def read(self):
        #For each location a code can be specified. The world pro trending code is 1

        self.trends = self.api.trends_place(1)
        self.trends = json.loads(json.dumps(self.trends, indent=1))
        
        for trend in self.trends[0]['trends']:
            self.trends_list.append({'text':trend['name'].strip('#')})

        return self.trends_list[0:10]

