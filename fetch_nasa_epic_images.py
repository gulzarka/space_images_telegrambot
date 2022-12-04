import requests
import os
import os.path
from urllib.parse import urlsplit, unquote
import datetime
import argparse
from download_images import download_images, get_file_extension


def get_epic_images():
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images",
                            params={"api_key": "DEMO_KEY"})
    response_content = response.json()
    for content in response_content:
        image_date = content['date'].split()[0].replace('-', '/')
        image_name = content['image']
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
        filename = f'{image_name}.{get_file_extension(image_link)}'
        path = 'epic_images/'
        params={"api_key": "DEMO_KEY"}
        download_images(image_link, path, filename, params=params)
        
get_epic_images()