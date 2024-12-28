import requests

directories = [
    'admin',
    'login',
    'config',
    'robots',
    'passwords',
]

url = 'http://192.168.1.11/mutillidae/'

for directory in directories:
    try:
        reqUrl = url + directory
        response = requests.get(reqUrl)
        status = response.status_code
        if response.status_code == 200:
            print(f'{url}{directory} - {str(status)} Berhasil')
        else:
            print(f'{url}{directory} - {str(status)} Error')

    except requests.exceptions.RequestException:
        pass