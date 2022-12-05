import requests
import os
import os.path
from urllib.parse import urlsplit, unquote
import argparse
from download_images import download_images, get_file_extension





def fetch_nasa_images():
    response = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY", "count": "10"})
    image_links = response.json()
    for image_number, image_link in enumerate(image_links):
        url = image_link['url']
        path = "nasa_images/"
        file_extension = get_file_extension(url)
        filename = f'{image_number}nasa_apod.{file_extension}'
        download_images(url,path,filename)

fetch_nasa_images()


