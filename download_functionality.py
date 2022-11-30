import os
from urllib.parse import urlparse

import requests
from pathlib import Path


def download_pic(dir_name, pic_name, url, pic_number):
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    filename = f"{dir_name}/{pic_name}_{pic_number}.jpg"

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def file_extension(url):
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext

# url = "https://example.com/txt/hello%20world.txt?v=9#python"
# print(file_extension(url))
