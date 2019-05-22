import csv
import re


class MiningLocation:
    def __init__(self, users_location):
        self.file_locations = list()
        self.locations = list()
        self.users_location = users_location
        self.read_csv_locations()

    def read_csv_locations(self):
        with open('tweets/api_twitter/datas/city_location.csv', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                self.file_locations.append({'city':row['city'],
                 'latitude':row['latitude'], 'longitude':row['longitude']})

    def treat_user_location(self): 
        for i in self.file_locations:
            regex = "^.*(\\b" + i['city'].lower() + "\\b).*?$"
            count = 0

            for j in self.users_location:
                if re.search(regex, j.lower()):
                    self.locations.append([i['latitude'], i['longitude']])
                    del(self.users_location[count])
                count += 1    

        return self.locations

