import datetime
import requests
from decouple import config
from download_functionality import download_pic


def fetch_fresh_earth_pics(api_key):
    pics_api_url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": api_key}
    response = requests.get(pics_api_url, params=payload)
    response.raise_for_status()
    picture_name = 'earth_pic'

    for pic_number, pic_data in enumerate(response.json()):
        date = datetime.datetime.fromisoformat(pic_data['date']).strftime('%Y/%m/%d')
        image = pic_data['image']
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png"
        download_pic(picture_name, pic_url, payload, pic_number)


if __name__ == '__main__':
    nasa_api_key = config('NASA_API_KEY')
    fetch_fresh_earth_pics(nasa_api_key)
