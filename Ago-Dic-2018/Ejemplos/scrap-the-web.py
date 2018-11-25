import requests, os, errno
from bs4 import BeautifulSoup

url = 'https://punkapi.com/documentation/v2'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
meta_tags = soup.find_all('meta')

for meta in meta_tags:
    # metas = BeautifulSoup(meta, 'html.parser')
    print(meta.get('content'))
# print([meta['content'] for meta in meta_tags])
