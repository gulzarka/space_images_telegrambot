import requests
from download_images import download_images
import argparse



def fetch_spacex_images(launch_id):
    response = requests.get("https://api.spacexdata.com/v5/launches/{0}".format(launch_id))
    response.raise_for_status()
    response_content = response.json()
    image_links = response_content['links']['flickr']['original']
    for number, image_link in enumerate(image_links):
        path = 'images'
        filename = f'{number}spacex.jpg'
        download_images(image_link, path, filename)


def create_arguments():
    parser = argparse.ArgumentParser(description='fetch_spacex_images arguments')
    parser.add_argument('-id', '--launch_id', default = 'latest', required=False, 
                        help='Put launch id, or default name "latest" will be used')
    argument = parser.parse_args()
    return argument.launch_id 
          
        
def main():
    launch_id = create_arguments()
    try:
        fetch_spacex_images(launch_id)
    except requests.exceptions.HTTPError:
        print('Invalid launch_id')

     
if __name__ == '__main__':
    main()

    





        

      



