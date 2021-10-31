import requests
from pathlib import Path


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}

    def set_dest_path(self, save_path):
        """Метод проверяет наличие папки save_path и, при необходимости создает ее"""
        res = requests.get(f'{self.url}?path=%2F{save_path}&preview_crop=true', headers=self.headers)
        if res.status_code == 404:
            resp = requests.put(f'{self.url}?path=%2F{save_path}', headers=self.headers)
            if resp.status_code == 201:
                return res.status_code, resp.status_code
            else:
                return res.status_code, False
        elif res.status_code == 200:
            return res.status_code, True

    def upload(self, source_path, save_path, list_photo):
        """Метод загружает файлы по списку list_photo на яндекс диск"""
        replace = True
        for photo in list_photo:
            file_spec = source_path / photo['file_name']
            yd_spec = save_path + '/' + photo['file_name']
            res = requests.get(f'{self.url}/upload?path={yd_spec}&overwrite={replace}', headers=self.headers).json()
            with open(file_spec, 'rb') as f:
                try:
                    print('Write:', yd_spec)
                    requests.put(res['href'], files={'file': f})
                except KeyError:
                    print(res)


if __name__ == '__main__':
    path_dir = Path.cwd() / 'images'
    file_list = []
    token_yd = '...'
    uploader = YaUploader(token_yd)
    yd_save_folder = input('Enter YD folder name for saved photo: ')
    res, lans = uploader.set_dest_path(yd_save_folder)
    if lans:
        uploader.upload(path_dir, yd_save_folder, file_list)
        print('Done')
    else:
        print(f'Problem with folder for saved photo <{yd_save_folder}>')
