import requests

def findSubdomain(domain, timeout=3):
    worldList = [
        'admin',
        'api',
        'blog',
        'chat',
        'image',
        'login',
        'mail',
    ]

    for subDomain in worldList:
        url = f'http://{subDomain}.{domain}'
        try:
            response = requests.get(url)
            status = response.status_code
            print(f'{url} - {status}')
        except requests.exceptions.RequestException:
            pass

        url = f'https://{subDomain}.{domain}'
        try:
            response = requests.get(url)
            status = response.status_code
            print(f'{url} - {status}')
        except requests.exceptions.RequestException:
            pass

domain = str(input('(Contoh: Google.com)\nMasukkan Domain: '))
timeout = 4

findSubdomain(domain, timeout)