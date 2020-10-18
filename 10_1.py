import requests

def get_intelegence(**hero):
    heros_dict = {}
    for he in hero.values():
        response = requests.get(f"https://superheroapi.com/api/2619421814940190/search/{he}")
        intelligence = response.json()['results'][0]['powerstats']['intelligence']
        heros_dict.update({he: intelligence})

    list_dict = list(heros_dict.items())
    list_dict.sort(key=lambda i: i[1])
    print(f'Самый умный - {list_dict[0][0]}')


get_intelegence(first = 'Captain America', second = 'Hulk', third = 'Thanos')
