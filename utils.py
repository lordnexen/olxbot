from warnings import showwarning
from telegram import error, ParseMode, InlineKeyboardMarkup, Update, replymarkup, update, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, callbackcontext, CallbackQueryHandler,ConversationHandler, commandhandler
from telegram.files.location import Location

import get_web
import model

SEARCHTEXT, SENDADV, SENDADV_PROKL, COLADV, MAKEDB = range(5)
zaloop = 0

def start(update,context):

    context.bot.send_message(chat_id = update.effective_chat.id, text = "Что я могу найти для тебя?")
    return SEARCHTEXT


def searchtext(update,context):

    global search_text
    search_text = update.message.text

    reply_keyboard = ReplyKeyboardMarkup([['Покажи результаты'],['Сохрани в базу данных'],["Изменить запрос"]], one_time_keyboard=True, resize_keyboard=True)

    context.bot.send_message(chat_id = update.effective_chat.id, text =f'Ищу <b>"{search_text}"</b>, показать результаты или собрать в базу данных?', reply_markup = reply_keyboard, parse_mode = ParseMode.HTML )
    
    return COLADV



def colect_advert(update,context):

   global adverts
   adverts = get_web.get_adverts('https://www.olx.ua/list/q-'+search_text)

   reply_keyboard = ReplyKeyboardMarkup([['5','10',"15"]], one_time_keyboard=True, resize_keyboard=True)
   context.bot.send_message(chat_id = update.effective_chat.id, text = 'Сколько результатов показать?', reply_markup=reply_keyboard)
   
   return SENDADV_PROKL
   


def send_advert_prokl(update, context):

    global counter
    counter=int(update.message.text)

    reply_keyboard = ReplyKeyboardMarkup([['Да, покажи'],['Сохрани в базу данных'],["Изменить запрос"]], one_time_keyboard=True, resize_keyboard=True)
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"<b>Обьявления собраны.</b> Показать первые <i>{counter}</i> результатов?", reply_markup=reply_keyboard, parse_mode=ParseMode.HTML)
    

    return SENDADV


def send_advert(update, context):
        
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"Вот что я нашел по запросу <b>{search_text}</b>", parse_mode=ParseMode.HTML)
    
    for i in range(counter):
        single_adv=adverts[i]
        text = """
<b>{title}</b>  
<i>Цена:</i> <b>{price}</b>
<i>Город:</i> <b>{location}</b> 
{url}""".format(**single_adv)
        try:
            context.bot.send_photo(chat_id = update.effective_chat.id, photo = single_adv['img'], caption = text,  parse_mode = ParseMode.HTML)
        except telegram.error.BadRequest:
            context.bot.send_message(chat_id = update.effective_chat.id, text = text, parse_mode=ParseMode.HTML)

    reply_keyboard = ReplyKeyboardMarkup([['Найди еще'],['Покажи больше обьявлений']], one_time_keyboard = True, resize_keyboard = True)
    context.bot.send_message(chat_id = update.effective_chat.id, text =  'Могу я найти для тебя что то еще или показать больше обьявлений?', reply_markup=reply_keyboard )



def create_db(update,context):

   reply_keyboard = ReplyKeyboardMarkup([['Да, собери'],["Изменить запрос"]], one_time_keyboard=True, resize_keyboard=True)
   context.bot.send_message(chat_id = update.effective_chat.id, text = "собрать полученные результаты в файл?", reply_markup = reply_keyboard)
   
   return MAKEDB


def make_db(update,context):

    adverts = get_web.get_adverts('https://www.olx.ua/list/q-'+search_text)
    
    context.bot.send_message(chat_id = update.effective_chat.id, text = "собираю базу данных")
    for single_adv in adverts:
        model.save_adv(single_adv['title'],single_adv['url'],single_adv['location'],single_adv['price'])


search = ConversationHandler(

    entry_points = [CommandHandler('start',start)],
    states ={
        SEARCHTEXT:[MessageHandler(Filters.text,searchtext)],
        COLADV: [MessageHandler(Filters.regex('^Покажи результаты$'),colect_advert)],
        SENDADV_PROKL: [MessageHandler(Filters.regex('^(5|10|15)$'),send_advert_prokl)],
        SENDADV:[MessageHandler(Filters.regex('^Да, покажи$'),send_advert),MessageHandler(Filters.regex('^Покажи больше обьявлений$'),send_advert),MessageHandler(Filters.regex('^Сохрани в базу данных$'),create_db)],
        MAKEDB: [MessageHandler(Filters.regex('^Да, собери$'),make_db)]
    },
    fallbacks = [MessageHandler(Filters.regex('^Изменить запрос$'),start), MessageHandler(Filters.regex('^Найди еще$'),start)]
)