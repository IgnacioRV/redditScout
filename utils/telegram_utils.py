import telegram
from config import config


token = config["BOT_TOKEN"]
bot = telegram.Bot(token=token)
chat_id = config["CHAT_ID"]
start_remove = 30


def send_message(text):
    global start_remove
    if start_remove > 0:
        start_remove -= 1
    else:
        bot.send_message(chat_id=chat_id, text=text)