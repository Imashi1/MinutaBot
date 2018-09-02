import telegram
from telegram.ext import *
from MinutaData import *

mi_bot = telegram.Bot(token='664910518:AAEcu4xoiAwX-CWXsn1LjS1xzkVT2YhJplQ')
mi_bot_updater = Updater(mi_bot.token)



def minuta(bot,update, pass_chat_data=True):
	update.message.chat_id
	actualizarArchivos()
	info = open('info.txt')
	minuta = ''.join(info.readlines())
	info.close()
	bot.sendMessage(chat_id=update.message.chat_id, text=minuta)

start_handler = CommandHandler('minuta',minuta)
dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)

mi_bot_updater.start_polling()
mi_bot_updater.idle()


