import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

token = os.environ['TELEGRAM_TOKEN']

bot = telegram.Bot(token=token)

updater = Updater(token=token)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Not dead yet")
    


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()