import requests
import os
import os.path
from urllib.parse import urlsplit, unquote
import datetime
import argparse
from download_images import download_images

def get_epic_images():
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images",
                            params={"api_key": "DEMO_KEY"})
    response_content = response.json()
    response.raise_for_status()
    for content in response_content:
        image_date = content['date'].split()[0].replace('-', '/')
        image_name = content['image']
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
        filename = f'{image_name}.png'
        path = 'images'
        params={"api_key": "DEMO_KEY"}
        download_images(image_link, path, filename, params=params)


def main():
    get_epic_images()
        
if __name__ == '__main__':
    main()