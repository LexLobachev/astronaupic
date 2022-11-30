import requests
import argparse
from download_functionality import download_pic


parser = argparse.ArgumentParser(
    description='Скачивает фото запуска spacex'
)
parser.add_argument('-l', '--launch', help='launch_id')


def fetch_spacex_last_launch(dir_name, api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    pics = response.json()['links']['flickr']['original']
    picture_name = 'spacex'

    for pic_number, pic_url in enumerate(pics):
        download_pic(dir_name, picture_name, pic_url, pic_number)


if __name__ == '__main__':
    args = parser.parse_args()
    directory_name = "images"
    if args.launch is not None:
        flight_number = args.launch
        space_api_url = f"https://api.spacexdata.com/v5/launches/{flight_number}"
    else:
        space_api_url = f"https://api.spacexdata.com/v5/launches/latest"
    fetch_spacex_last_launch(directory_name, space_api_url)

# flight_number = '5eb87d42ffd86e000604b384'
