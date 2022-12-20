import os
from os import path
import requests
from urllib.parse import urlsplit, unquote


def download_images(url, path, filename, params):
    response = requests.get(url, params=None)
    response.raise_for_status()
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename),'wb') as file:
        file.write(response.content)


