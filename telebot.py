import telegram
from decouple import config

bot = telegram.Bot(token=config('TELEGRAM_TOKEN'))
print(bot.get_me())

bot.send_message(text='Hi everybody!', chat_id='@astronaupic')