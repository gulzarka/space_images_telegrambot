import requests
import os
from urllib.parse import urlsplit
import argparse
from dotenv import load_dotenv
from download_images import download_images


def get_file_extension(url):
    parsed_url = urlsplit(url)
    file_extension = os.path.splitext(parsed_url.path)[-1]
    return file_extension


def fetch_nasa_images(access_token, count):
    response = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": access_token, "count": count})
    response.raise_for_status()
    image_links = response.json()
    for image_number, image_link in enumerate(image_links):
        media_type = image_link["media_type"]
        if media_type != "image":
            continue
        url = image_link["url"]
        path = "images"
        file_extension = get_file_extension(url)
        filename = f"{image_number}nasa_apod{file_extension}"
        download_images(url, path, filename)


def create_argument():
    load_dotenv("tokens.env")
    parser = argparse.ArgumentParser(description="Downloads NASA APOD images")
    parser.add_argument(
        "-t", "--token", default=os.environ["NASA_API_KEY"], required=False, help="use -t or --token and put your token; default"
    )
    parser.add_argument(
        "-n",
        "--number",
        default=1,
        required=False,
        type=int,
        help="use -n or --number and put needed number for downloading images",
    )
    argument = parser.parse_args()
    return argument


def main():
    args = create_argument()
    count = args.number
    access_token = args.token
    try:
        fetch_nasa_images(access_token, count)
    except requests.exceptions.HTTPError:
        print("Http error is occured....")


if __name__ == "__main__":
    main()
