import logging
import os
import time
import random

import telegram
from decouple import config
import argparse

from telegram.error import NetworkError

parser = argparse.ArgumentParser(
    description='Постит фотографии в телеграмм'
)
parser.add_argument('-hh', '--hours', help='amount_of_hours', default=4, type=int)
parser.add_argument('-pn', '--picture', help='exact picture or random', default='random', type=str)


def post_pictures(chat, folder, token, hours, pic_name):
    bot = telegram.Bot(token=token)
    images_list = os.listdir(folder)

    if pic_name == 'random':
        while True:
            for picture in images_list:
                with open(f'{os.path.join(folder, picture)}', 'rb') as document:
                    try:
                        bot.send_document(chat_id=chat, document=document)
                    except NetworkError as e:
                        logging.error(f'Problem with network connection! \n{e}')
                time.sleep(hours)
            random.shuffle(images_list)
    else:
        with open(f'{os.path.join(folder, pic_name)}', 'rb') as document:
            try:
                bot.send_document(chat_id=chat, document=document)
            except NetworkError as e:
                logging.error(f'Problem with network connection! \n{e}')


if __name__ == '__main__':
    args = parser.parse_args()
    folder_name = "images"
    chat_id = config('TG_CHAT_ID')
    tg_token = config('TELEGRAM_TOKEN')
    hours_amount = args.hours
    picture_name = args.picture
    post_pictures(chat_id, folder_name, tg_token, hours_amount, picture_name)
