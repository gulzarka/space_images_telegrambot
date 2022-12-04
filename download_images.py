import os
from os import path
import requests
from urllib.parse import urlsplit, unquote


def download_images(url, path, filename, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename),'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    parsed_url = urlsplit(url)
    file_extension = os.path.splitext(parsed_url.path)[-1]
    filename = unquote(os.path.split(parsed_url.path)[-1])
    return file_extension