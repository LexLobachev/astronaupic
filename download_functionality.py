import os
from urllib.parse import urlparse

import requests
from pathlib import Path


def download_pic(pic_name, url, payload, pic_number):
    dir_name = "images"
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    pic_name = f"{pic_name}_{pic_number}.{get_file_extension(url)}"
    filename = os.path.join(dir_name, pic_name)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext
