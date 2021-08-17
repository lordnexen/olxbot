from re import I
from warnings import showwarning

from telegram import InputMediaPhoto,error, ParseMode, InlineKeyboardMarkup, Update, replymarkup, update, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, callbackcontext, CallbackQueryHandler,ConversationHandler, commandhandler


import get_web
import model

SEARCHTEXT, SENDADV, SENDADV_PROKL, COLADV, MAKEDB, SEARCHCONTEXT= range(6)
i = 0

PREV,NEXT = range(2)

inline_keyboard = [
        [
            InlineKeyboardButton("Предыдущее обьявление", callback_data=str(PREV), i=i-1),
            InlineKeyboardButton("Следующее обьявление", callback_data=str(NEXT), i=i+1),
        ]
    ]



def start(update,context):

    reply_keyboard = ReplyKeyboardMarkup([['Поиск по обьявлениям'],['Поиск по категории']],
        one_time_keyboard=True,
        resize_keyboard=True)

    context.bot.send_message(
        chat_id = update.effective_chat.id, 
        text = "Как будем искать?",
        reply_markup = reply_keyboard
          )
    
    return SEARCHCONTEXT


def searchcontext(update,context):

    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'Что будем искать?')
    
    return SEARCHTEXT




def searchtext(update,context):

    global search_text
    search_text = update.message.text

    reply_keyboard = ReplyKeyboardMarkup(
        [['Все верно'],["Изменить запрос"]],
        one_time_keyboard=True,
        resize_keyboard=True
        )

    context.bot.send_message(
    chat_id = update.effective_chat.id,
    text =f'Ищу <b>"{search_text}"</b>, все верно?',
    reply_markup = reply_keyboard, 
    parse_mode = ParseMode.HTML 
    )
    
    return COLADV



def colect_advert(update,context):

    global adverts
    chat_id = update.effective_chat.id
    try:
        adverts = get_web.get_adverts('https://www.olx.ua/list/q-'+search_text, chat_id)
    
    except UnboundLocalError:
        reply_keyboard = ReplyKeyboardMarkup([["Изменить запрос"]])
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text ="Ничего не найдено",
            reply_markup = reply_keyboard
            )

   
    reply_keyboard = ReplyKeyboardMarkup(
        [['Да, покажи'],['Сохрани в базу данных'],["Изменить запрос"]],
        one_time_keyboard=True,
        resize_keyboard=True
        )

    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f"<b>Обьявления собраны.</b> Показать?", 
        reply_markup=reply_keyboard, parse_mode=ParseMode.HTML
        )

    return SENDADV
   


def send_advert_prokl(update, context):

    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    single_adv=adverts[0]
    print(single_adv)
    global chat_id
    chat_id = update.effective_chat.id

    
    print(chat_id)
    text = """
        <b>{title}</b>  
        <i>Цена:</i> <b>{price}</b>
        <i>Город:</i> <b>{location}</b> 
        {url}""".format(**single_adv)

    context.bot.send_photo(
        chat_id = update.effective_chat.id,
        caption = f"Вот что я нашел по запросу <b>{search_text}</b>, {text}", 
        parse_mode=ParseMode.HTML,
        reply_markup = reply_markup,
        photo = single_adv['img']
        )


    global i
    i=i+1
    
    
    return SENDADV


def send_advert(update, context):
        
    query = update.callback_query
    
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    print (query.data)
    
    global i
   
    
    try:
        chat_id = update.effective_chat.id
        if query.data == '0' and i>0:

            i=i-1

            single_adv=adverts[i]
        
            print(chat_id)
            text = """
        <b>{title}</b>  
        <i>Цена:</i> <b>{price}</b>
        <i>Город:</i> <b>{location}</b> 
        {url}""".format(**single_adv)

            query.message.edit_media(
                media = InputMediaPhoto(
                    media = single_adv['img'],
                    caption=text,
                    parse_mode=ParseMode.HTML
                    ),
                reply_markup=reply_markup
                )
            
            query.answer()
            

        elif query.data == '1':

            i=i+1

            single_adv=adverts[i]
           
            text = """
        <b>{title}</b>  
        <i>Цена:</i> <b>{price}</b>
        <i>Город:</i> <b>{location}</b> 
        {url}""".format(**single_adv)
        
            query.message.edit_media(
                media = InputMediaPhoto(
                    media = single_adv['img'],
                    caption=text,
                    parse_mode=ParseMode.HTML
                    ), 
                reply_markup=reply_markup)

            query.answer()
            

    except telegram.error.BadRequest:

        query.message.edit_media(
            media = InputMediaPhoto(
                media = "https://retinaks.ru/files/default_images/nofoto.png",
                caption = text,
                parse_mode=ParseMode.HTML
                ),
            reply_markup=reply_markup
            )
   
    except IndexError:
        query.message.edit_media(
            media = InputMediaPhoto(
            media = "https://retinaks.ru/files/default_images/nofoto.png",
            caption = "Это все",
            parse_mode=ParseMode.HTML
            ),
        reply_markup=reply_markup
            )
            


def create_db(update,context):

   reply_keyboard = ReplyKeyboardMarkup(
       [['Да, собери'],["Изменить запрос"]],
       one_time_keyboard=True,
       resize_keyboard=True
       )
   context.bot.send_message(
       chat_id = update.effective_chat.id,
       text = "Cобрать полученные результаты в файл?",
       reply_markup = reply_keyboard
       )
   
   return MAKEDB


def make_db(update,context):

    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Cобираю базу данных"
        )

    for single_adv in adverts:
        model.save_adv(
            title = single_adv['title'],
            url = single_adv['url'],
            location = single_adv['location'],
            price = single_adv['price'],
            chat_id = single_adv['chat_id']
            )


search = ConversationHandler(

    entry_points = [CommandHandler('start',start)],
    states ={
        SEARCHCONTEXT:[MessageHandler(Filters.regex('^Поиск по обьявлениям'),searchcontext)],

        SEARCHTEXT:[MessageHandler(Filters.text,searchtext)],

        COLADV: [MessageHandler(Filters.regex('^Все верно$'),colect_advert)],

        SENDADV_PROKL: [MessageHandler(Filters.regex('^Да, покажи$'),send_advert_prokl)],

        SENDADV:[
            MessageHandler(Filters.regex('^Сохрани в базу данных$'),create_db),
            CallbackQueryHandler(send_advert) 
            ],

        MAKEDB: [MessageHandler(Filters.regex('^Да, собери$'),make_db)]
    },
    fallbacks = [
        MessageHandler(Filters.regex('^Изменить запрос$') | Filters.command,start),
        MessageHandler(Filters.regex('^Найди еще$'),start),
        MessageHandler(Filters.text,searchtext)
        ]
)