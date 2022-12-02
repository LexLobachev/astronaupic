import requests
import argparse
from decouple import config
from download_functionality import download_pic

parser = argparse.ArgumentParser(
    description='Скачивает астрономическую картинку дня'
)
parser.add_argument('-c', '--count', help='count_of_pics', default=5, type=int)


def fetch_multiple_nasa_pics(dir_name, url, api_key, count):
    payload = {"api_key": api_key,
               "count": count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    picture_name = 'nasa_apod'

    for pic_number in range(count):
        pic_url = response.json()[pic_number]['url']
        download_pic(dir_name, picture_name, pic_url, pic_number)


if __name__ == '__main__':
    args = parser.parse_args()
    directory_name = "images"
    api_url = "https://api.nasa.gov/planetary/apod"
    nasa_api_key = config('NASA_API_KEY')
    count_of_pics = args.count
    fetch_multiple_nasa_pics(directory_name, api_url, nasa_api_key, count_of_pics)
