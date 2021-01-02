import json
from pprint import pprint
import requests

data = requests.get('https://raw.githubusercontent.com/mledoze/countries/master/countries.json').json()
countries = [i['name']['official'] for i in data]

class MyIter:

    def __init__(self, countries_list):
        self.countries_list = countries_list
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == len(self.countries_list):
            raise StopIteration
        name = self.countries_list[self.cursor]
        self.cursor += 1
        ref = name.replace(" ", "_")
        return f'{name} - https://en.wikipedia.org/wiki/{ref}'



iter = MyIter(countries)

with open('countries-refs.txt', 'w') as file:
    for item in iter:
        file.write(item)
        file.write('\n')






