import datetime
import requests
from decouple import config
from download_functionality import download_pic


def fetch_fresh_earth_pics(dir_name, url, api_key):
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    picture_name = 'earth_pic'

    for pic_number, pic_data in enumerate(response.json()):
        date = datetime.datetime.fromisoformat(pic_data['date']).strftime('%Y/%m/%d')
        image = pic_data['image']
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={api_key}"
        download_pic(dir_name, picture_name, pic_url, pic_number)


if __name__ == '__main__':
    directory_name = "images"
    api_url = "https://api.nasa.gov/EPIC/api/natural/images"
    nasa_api_key = config('NASA_API_KEY')
    fetch_fresh_earth_pics(directory_name, api_url, nasa_api_key)
