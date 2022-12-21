# CosmoBot

Set of scripts. You can download space photos from NASA and spacex launches. Then you can post this photos in your
telegram channel.

## Environment

### Requirements

Python3(python 3.11 is recommended) should be already installed. Then use pip3 to install dependencies:

```bash
pip3 install -r requirements.txt
```

### Environment variables

- NASA_API_KEY
- TELEGRAM_TOKEN
- TG_CHAT_ID

1. Put `.env` file near `requirements.txt`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
NASA_API_KEY=WLNJeZjPhkbBS1HLzDuY6ylzp5Pxo0GnFkVJjyvz
TELEGRAM_TOKEN=9476281456:AAH2Qc4a1OUshqoilWsk3GSw82ZUR6yhX8s
TG_CHAT_ID=@astronaut_pics
```

#### How to get

* Register an application [NASA APIs](https://api.nasa.gov/#signUp) and generate there the `Api Key`
* To generate a Telegram Access Token, you have to talk to [BotFather](https://t.me/botfather) and follow a few simple
  steps (
  described [here](https://core.telegram.org/bots#6-botfather))
* TG_CHAT_ID is just a chat name, like in the example @astronaut_pics

## Run

Launch on Linux(Python 3) or Windows:

### fetch_apod_images.py

Script for downloading random Astronomy Picture of the Day from NASA

```bash
$ python3 fetch_apod_images.py
```

You will receive 5 photos in created directory called `images`

If you want to download another amount of pictures(for example 10):

```bash
$ python3 fetch_apod_images.py -c 10
```

### fetch_epic_images.py

Script for downloading EPIC(Earth Polychromatic Imaging Camera) photos of yesterday's Earth from NASA

```bash
$ python3 fetch_epic_images.py
```

You will receive yesterday photos of Earth in created directory called `images`

### fetch_spacex_images.py

Script for downloading photos of SpaceX launches

```bash
$ python3 fetch_spacex_images.py
```

You will receive the latest photos of launches in created directory called `images`

If you want to download photos from exact launch(for example 5eb87d42ffd86e000604b384):

```bash
$ python3 fetch_spacex_images.py -l 5eb87d42ffd86e000604b384
```

### telebot.py

Script for uploading photos from `images` folder to telegram channel

```bash
$ python3 telebot.py
```

The script will first put the photos from the folder in direct order with the default interval of 4 hours, then it will
endlessly post the photos in random order

If you want to download photos in other interval(for example 2 hours):

```bash
$ python3 telebot.py -h 2
```

Or if you want to post an exact photo(for example nasa_apod_4.jpg):

```bash
$ python3 telebot.py -pn nasa_apod_4.jpg
```

## Brief summary of other files
### download_functionality.py

function for downloading a picture and function for receiving file extension
