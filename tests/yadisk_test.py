

import unittest
import requests

with open('TOKEN.txt', 'r') as token_file:
     TOKEN_YADISK  = token_file.readline()
mkdir_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.put(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN_YADISK}
    create_dir = requests.api.delete(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(create_folder(''), 201)
        print('Папка создана')

    def test_passed_create_folder(self):
        self.assertEqual(create_folder('TESTS_P'), 409)

    def tearDown(self):
        # Удаляем папку после прохождения теста на создание папки
        delete_folder('')
        print('Папка удалена')


if __name__ == '__main__':
    unittest.main()



