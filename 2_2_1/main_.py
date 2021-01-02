import json
from pprint import pprint
import requests

# class MyIter:
#
#     def __init__(self, countries_list):
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):


path = 'countries.json'
with open(path, 'r') as f:
    data = json.loads(f.read())
    countries = [i['name']['official'] for i in data]

pair = []

for count in countries:
    ref = count.replace(' ','_')
    pair.append(f'{count}  -  https://en.wikipedia.org/wiki/{ref}')

with open('countries-refs.txt', 'w') as file:
    for items in pair:
        file.write(items)
        file.write('\n')






