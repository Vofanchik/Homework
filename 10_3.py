import requests
import time
today = str(time.time()).split('.')[0]
two_d_ago = int(today) - 86400

response = requests.get("https://api.stackexchange.com/2.2/questions", params={'fromdate': two_d_ago, 'todate': today, 'tagged': 'Python', 'site': 'stackoverflow'})

for i in response.json()['items']:
    print(i['title'])
