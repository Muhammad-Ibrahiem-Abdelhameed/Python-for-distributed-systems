import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request
import re

logger = logging.getLogger(__name__)



def get_links(url):
    #headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    headers = {
        'User-Agent':
            'Mozilla/5.0 AppleWebKit/538.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/538.36'
    }
    req = Request(url, headers=headers)
    with urlopen(req) as resp:
        data = resp.read()
    #return [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]
    regex = b'href="\/[a-zA-Z\S]*"'
    links = []
    for i in re.findall(regex, data):
        raw_str1 = str(i).split('"')[1]
        if not raw_str1.endswith(('png', 'jpg', 'json', 'css', '#', '/')) and not raw_str1.startswith('//') :
            links.append(str(i).split('"')[1])
    return links

def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)


def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir

def setup_url_file():
    file = Path('urls.txt')
    if not file.exists():
        file.open('w+')
