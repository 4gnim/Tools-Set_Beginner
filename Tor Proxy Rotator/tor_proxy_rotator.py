import time
import requests
from stem.control import Controller

def get_tor_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # Ganti dengan password Tor Anda
        controller.signal(2)  # Signal NEWNYM untuk mengganti IP
        print("[+] IP Address changed!")

if __name__ == "__main__":
    while True:
        renew_tor_ip()
        session = get_tor_session()
        try:
            response = session.get("http://check.torproject.org")
            print("[+] Current IP:", response.text)
        except requests.RequestException as e:
            print("[-] Error:", e)
        time.sleep(10)  # Tunggu 10 detik sebelum mengganti IP lagi
