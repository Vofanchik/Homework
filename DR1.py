import requests
import json
import tqdm

user_input_1 = input('Введите токен Яндекс.Диск: ')
user_input_2 = input('Введите ID пользователя ВК, чьи фото должны быть загружены: ')
user_input_3 = input('Введите название папки для Яндекс.Диск : ')

class VkUploader:
    def __init__(self, token: str, owner_id: int, folder_name: str):
        self.token = token
        self.owner_id = owner_id
        self.folder_name = folder_name
        self.HEADERS = {"Authorization": f"OAuth {self.token}"}

    def get_info(self):

        photo_urls, likes, size = [], [], []

        response = requests.get("https://api.vk.com/method/photos.get",
                                params={'owner_id': self.owner_id,
                                        'extended': 1,
                                        'album_id': 'profile',
                                        'count': 5,
                                        'v': 5.124,
                                        'access_token': '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'})

        data = response.json()['response']['items']

        for post in data:
            photo_urls.append(post['sizes'][-1]['url'])
            if post['likes']['count'] in likes:
                likes.append(post['likes']['count'] + 1)
            else:
                likes.append(post['likes']['count'])
            size.append(post['sizes'][-1]['type'])

        url_name_size = list(zip(photo_urls, likes, size))

        return url_name_size

    def create_folder(self):
        requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                              headers = self.HEADERS,
                              params={'path': f'disk:/{self.folder_name}'})

    def upload_photos(self):
        self.create_folder()
        for photo in tqdm.tqdm(self.get_info()):
            requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                 headers = self.HEADERS,
                                 params = {'path': f'disk:/{self.folder_name}/{photo[1]}.jpg',
                                         'url': f'{photo[0]}'})

            print(json.dumps([{
                "file_name": f"{photo[1]}.jpg",
                "size": f"{photo[2]}"
            }]))

uploader = VkUploader(user_input_1, user_input_2, user_input_3)
uploader.upload_photos()




