import os
import requests


def download_images(url, path, filename, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, filename), "wb") as file:
        file.write(response.content)
