import requests
import argparse
from download_functionality import download_pic


parser = argparse.ArgumentParser(
    description='Скачивает фото запуска spacex'
)
parser.add_argument('-l', '--launch', default='latest', help='launch_id')


def fetch_spacex_last_launch(flight_num):
    pics_api_url = f"https://api.spacexdata.com/v5/launches/{flight_num}"
    response = requests.get(pics_api_url)
    response.raise_for_status()
    pics = response.json()['links']['flickr']['original']
    picture_name = 'spacex'

    for pic_number, pic_url in enumerate(pics):
        download_pic(picture_name, pic_url, '', pic_number)


if __name__ == '__main__':
    args = parser.parse_args()
    flight_number = args.launch
    fetch_spacex_last_launch(flight_number)
