# import json
# from pprint import pprint
# import requests
#
# # class MyIter:
# #
# #     def __init__(self, countries_list):
# #
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
#
#
# path = 'countries.json'
# with open(path, 'r') as f:
#     data = json.loads(f.read())
#     countries = [i['name']['common'] for i in data]
#
# pair = []
# file_obj=0
#
# for count in countries:
#     response = requests.get('https://en.wikipedia.org/w/api.php', params={"search": count, "action": "opensearch", "format": "json", "inprop": "url"})
#     pair.append(f'{count}-{response.json()[3][0]}')







