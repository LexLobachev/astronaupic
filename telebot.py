import os
import time
import random

import telegram
from decouple import config
import argparse

parser = argparse.ArgumentParser(
    description='Постит фотографии в телеграмм'
)
parser.add_argument('-h', '--hours', help='amount_of_hours', const=4, type=int)


def post_pictures(chat, folder, token, hours):
    bot = telegram.Bot(token=token)
    images_list = os.listdir(folder)

    while True:
        for picture in images_list:
            with open(f'{folder}/{picture}', 'rb') as document:
                bot.send_document(chat_id=chat, document=document)
            time.sleep(3600*hours)
        random.shuffle(images_list)


if __name__ == '__main__':
    args = parser.parse_args()
    folder_name = "images"
    chat_id = config('CHAT_ID')
    tg_token = config('TELEGRAM_TOKEN')
    hours_amount = args.hours
    post_pictures(chat_id, folder_name, tg_token, hours_amount)
