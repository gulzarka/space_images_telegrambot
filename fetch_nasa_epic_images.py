import os
import requests
import argparse
from datetime import datetime
from dotenv import load_dotenv
from download_images import download_images


def get_epic_images(access_token):
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images",
                            params={"api_key": access_token})
    response_content = response.json()
    response.raise_for_status()
    for content in response_content:
        image_date = datetime.fromisoformat(content['date'])
        formatted_image_date = image_date.strftime('%Y/%m/%d')
        image_name = content['image']
        image_link = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_image_date}/png/{image_name}.png"
        filename = f'{image_name}.png'
        path = 'images'
        params={"api_key": access_token}
        download_images(image_link, path, filename, params=params)
 

def create_argument():
    load_dotenv('tokens.env')
    access_token = os.environ['API_KEY']
    parser = argparse.ArgumentParser(description='Downloads NASA APOD images')
    parser.add_argument('-t', '--token', default=access_token, required=False, 
                        help= 'use -t or --t and put your token or default token will be run' )
    argument = parser.parse_args()
    return argument.token                    


def main():
    access_token = create_argument()
    try:
        get_epic_images(access_token)
    except requests.exceptions.HTTPError:
        print('Http error is occured....')       

        
if __name__ == '__main__':
    main()