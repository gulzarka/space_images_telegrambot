import requests
import os
import os.path
from urllib.parse import urlsplit, unquote
import argparse
from download_images import download_images

def get_file_extension(url):
    parsed_url = urlsplit(url)
    file_extension = os.path.splitext(parsed_url.path)[-1]
    return file_extension


def fetch_nasa_images(count):
    response = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY", "count": count })
    response.raise_for_status()
    image_links = response.json()
    for image_number, image_link in enumerate(image_links):
        media_type = image_link['media_type']
        if media_type != 'image':
            continue
        url = image_link['url']   
        path = "images"
        file_extension = get_file_extension(url)
        filename = f'{image_number}nasa_apod{file_extension}'
        download_images(url,path,filename)


def create_argument():
    parser = argparse.ArgumentParser(description='argument for choosing number of images to download')
    parser.add_argument('-n', '--number', default=1, required=False,
                        help='use -n or --number and put needed number for downloading images')
    argument = parser.parse_args()
    return argument.number                 


def main():
    count = create_argument() 
    try:
       fetch_nasa_images(count)
    except requests.exceptions.HTTPError:
        print('Http error is occured....')    
        

if __name__ == '__main__':
    main()

