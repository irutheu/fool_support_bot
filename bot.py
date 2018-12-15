import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ['TELEGRAM_TOKEN']

bot = telegram.Bot(token=token)

updater = Updater(token=token)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Not dead yet')

start_handler = CommandHandler('start', startCommand)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()

