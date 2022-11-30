import telegram
from decouple import config

bot = telegram.Bot(token=config('TELEGRAM_TOKEN'))
print(bot.get_me())

bot.send_document(chat_id='@astronaupic', document=open('images/nasa_apod_0.jpg', 'rb'))
