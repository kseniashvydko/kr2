import os
import requests
import concurrent.futures as pool

resp = requests.get('https://api.ipify.org/?format=json')
user_ip = resp.json()['ip']

user_ip_info = requests.get(url='https://ipinfo.io/' + user_ip + '/geo')

dir = f'user_data/{user_ip}/'
os.makedirs(dir, exist_ok=True)

with open(os.path.join(dir, 'user_info.txt'), 'w', encoding='utf-8') as file:
    file.write(user_ip_info.text)

def download_doge():
    s = requests.Session()
    r = s.get('https://dog.ceo/api/breeds/image/random')
    img_url = r.json()
    r = s.get(img_url['message'])
    with open(os.path.join(dir, r.url.split('/')[-1]), 'wb') as f:
        f.write(r.content)

with pool.ThreadPoolExecutor(4) as pool:
    for _ in range(12):
        pool.submit(download_doge)