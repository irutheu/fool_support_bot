import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

bot = telegram.Bot(token='')

updater = Updater(token='')
print(bot.get_me())


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Not dead yet')
    
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()