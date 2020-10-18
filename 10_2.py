import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path.split('\\')[-1]
        HEADERS = {"Authorization": f"OAuth {self.token}"}
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": f"{file_name}"},
            headers=HEADERS)

        try:
            upload_file = requests.put(response.json()['href'], files = {'file': open(file_path, 'rb')})
            if upload_file.status_code == 201:
                return print(f'фаил {file_path} загружен')
            else:
                return print(f'ошибка {upload_file.status_code}')
        except:
            return print('ошибка, возможно, фаил уже загружен')

uploader = YaUploader('')
result = uploader.upload(r'c:\my_folder\file.txt')
