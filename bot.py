import logging
from re import A
import re
from requests.api import get

from telegram import ParseMode, InlineKeyboardMarkup, Update, replymarkup, update, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, callbackcontext, CallbackQueryHandler,ConversationHandler, commandhandler
from telegram.files.location import Location


import config
import utils

SEARCHTEXT, SENDADV, SENDADV_PROKL, COLADV, MAKEDB = range(5)

logging.basicConfig(format='%(asctime)s - %(levelname)s -%(message)s',
level=logging.INFO,
filename='bot.log'
)




def main():

    mybot = Updater(config.API_KEY)
    
    logging.info('Bot is started')
    
    dp= mybot.dispatcher
   
    dp.add_handler(utils.search)
    
    
    
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()