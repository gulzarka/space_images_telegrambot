import os
import time
import random
import argparse

import telegram
from dotenv import load_dotenv

def send_image(bot, channel, directory, file):
    with open(os.path.join(directory, file), 'rb') as image:
         bot.send_photo(chat_id=channel, photo=image)


def post_selected_image(bot, channel, file):
    directory = 'images'
    send_image(bot, channel, directory, file)
    

def post_shuffled_images(bot, channel, directory, timer=14400):
    while True:
        files = list(os.walk(directory))[0][2]
        random.shuffle(files)
        for file in files:
            send_image(bot,channel,directory,file)
            time.sleep(int(timer))
            time.sleep(15)
            
       

         
def create_arguments():
    parser = argparse.ArgumentParser(description='Post images to telegram channel')
    parser.add_argument(
        '-t',
        '-timer',
        default=14400,
        required=False,
        help='Timer in seconds. Default: 14400'
    )
    parser.add_argument(
        '-f',
        '-folder',
        default='images',
        required=False,
        help='Image folder. Default: images'
    )
    parser.add_argument(
        '-i',
        '-image',
        required=False,
        help='Specific image to upload'
    )
    args = parser.parse_args()
    return args


def main():
    load_dotenv('tokens.env')
    telegram_bot_token = os.environ['TELEGRAMBOT_TOKEN']
    channel = os.environ['TELEGRAM_CHANNEL']
    bot = telegram.Bot(token=telegram_bot_token)
    args = create_arguments()
    timer = args.t
    folder = args.f
    image = args.i
    if image:
        try:
            post_selected_image(bot, channel, image)
        except telegram.error.TelegramError:
            print('Telegram network error has occured')
    else:
        try:
            post_shuffled_images(bot, channel, folder, timer)     
        except telegram.error.TelegramError:
            print('connection error occured')
            
   


if __name__ == '__main__':
    main()
