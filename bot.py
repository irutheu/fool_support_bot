import telegram
import os
#import numpy as np
#import cv2
#import h5py
#from tensorflow import keras
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ['TELEGRAM_TOKEN']

#bot = telegram.Bot(token=token)

updater = Updater(token=token)
dispatcher = updater.dispatcher

# reading model from json file
#model = keras.models.load_model('model.h5')

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Not dead yet')

start_handler = CommandHandler('start', startCommand)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def fashion(bot, update):
	image = bot.getFile(update.message.photo[-1].file_id)
	
	bot.send_photo(chat_id=update.message.chat_id, photo = image)
	
fashion_handler = MessageHandler(Filters.photo, fashion)
dispatcher.add_handler(fashion_handler)

updater.start_polling()



