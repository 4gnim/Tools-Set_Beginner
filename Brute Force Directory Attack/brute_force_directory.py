import requests
import argparse
import time

def brute_force_directory(url, wordlist, delay):
    print(f'Starting directory brute force attack on {url}\n')

    try:
        with open(wordlist, 'r') as file:
            directories = file.readlines()
    except FileNotFoundError:
        print(f'Error: Wordlist File "{wordlist}" not found!')
        return
    
    for directory in directories:
        directory = directory.strip()
        full_url = f'{url}/{directory}'

        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f'[+] Found: {full_url}')
            elif response.status_code == 403:
                print(f'[-] Forbidden: {full_url}')
            else:
                print(f'[-] Not Found: {full_url} (Status Code: {response.status_code})')
        except requests.exceptions.RequestException as e:
            print(f'Error accessing {full_url}: {e}')
            break

        # Jeda Antar Permintaan
        time.sleep(delay)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Brute Force Directory Attack Tool')
    parser.add_argument('url', help='Target URL (e.g., http://example.com)')
    parser.add_argument('wordlist', help='path to the wordlist file')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay between requests (in seconds)')
    args = parser.parse_args()

    brute_force_directory(args.url, args.wordlist, args.delay)