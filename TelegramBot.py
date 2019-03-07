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

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Te da lata ir a revisar los almuerzos por la pagina o presencialmente, yo te puedo ayudar!. Solo escribe /minuta\n\n Creadores: Fabián Bugueño / Kevin Lagos\n\n Puedes checkear el repositorio de github en github.com/Imashi1/MinutaBot")

def venta(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="También tenemos frutas y verduras a la venta para hacer de tu experiencia culinaria, la mejor posible.\n\n Frutas\n\n Uva 1Kg $1000\n Tomate 1 Kg $700\n\n Verduras\n\n Cebolla 1Kg $500\n Zanahoria 1Kg $500\n Papas 1 Kg $500\n Pimentón c/u $200\n Choclo c/u $200\n Lechuga c/u $500 ")
minuta_handler = CommandHandler('minuta',minuta)
start_handler = CommandHandler('start',start)
venta_handler = CommandHandler('venta',venta)
dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(minuta_handler)

mi_bot_updater.start_polling()
mi_bot_updater.idle()


