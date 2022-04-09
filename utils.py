import queue
import re
from warnings import showwarning
from queue import Queue


from telegram import InputMediaPhoto,error, ParseMode, InlineKeyboardMarkup, Update, replymarkup, update, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, callbackcontext, CallbackQueryHandler,ConversationHandler, commandhandler
from telegram.ext.dispatcher import run_async

import json

import get_web
import model
import keyboards


SEARCHTEXT, SENDADV, SENDADV_PROKL, COLADV, MAKEDB, SEARCHCONTEXT, CATEGORIES= range(7)
i = 41
j = 0
page_counter = 1

PREV,NEXT = range(2)


queue = Queue()

def start(update,context):

    context.bot.send_message(
        chat_id = update.effective_chat.id, 
        text = "Введите поисковый запрос",
        )
    
    return SEARCHCONTEXT


def categories_start(update,context):

    context.bot.send_message(
        chat_id = update.effective_chat.id, 
        text = "Выберите категорию для поиска!!",
        reply_markup = keyboards.categories_keyboard
          )
    
    return CATEGORIES
    

def categories(update, context):

    query = update.callback_query

    if query.data == 'back':
        
        query.message.edit_text(
            text='Выберите категорию',
            parse_mode=ParseMode.HTML, 
            reply_markup = keyboards.categories_keyboard 
        )
        
    elif query.data == 'child':

        query.message.edit_text(
            text='Выбрана категория : <b>Дети</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/detskiy-mir'
        queue.put(search_link)
       
    elif query.data == 'estate':

        query.message.edit_text(
            text='Выбрана категория <b>Недвижимость</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/nedvizhimost'
        queue.put(search_link)
    
    elif query.data == 'auto':

        query.message.edit_text(
            text='Выбрана категория <b>Автомобили</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )  
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/transport'
        queue.put(search_link)

    elif query.data == 'parts':

        query.message.edit_text(
            text='Выбрана категория <b>Запчасти</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        ) 
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/zapchasti-dlya-transporta'
        queue.put(search_link)

    elif query.data == 'animals':

        query.message.edit_text(
            text='Выбрана категория <b>Животные</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        
        ) 
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/zhivotnye'
        queue.put(search_link)

    elif query.data == 'house':

        query.message.edit_text(
            text='Выбрана категория <b>Дом и Сад</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
            
        ) 
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/dom-i-sad'
        queue.put(search_link)

    elif query.data == 'elect':

        query.message.edit_text(
            text='Выбрана категория <b>Техника</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
            
        ) 
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/elektronika'
        queue.put(search_link)

    elif query.data == 'fashion':
        
        query.message.edit_text(
            text='Выбрана категория <b>Мода и стиль</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/moda-i-stil'
        queue.put(search_link)

    elif query.data == 'hobby':

        query.message.edit_text(
            text='Выбрана категория <b>Хобби</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/hobbi-otdyh-i-sport'
        queue.put(search_link)
    
    elif query.data == 'job':
        query.message.edit_text(
            text='Выбрана категория <b>Работа</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward    
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/rabota'
        queue.put(search_link)
    
    elif query.data == 'free':
        query.message.edit_text(
            text='Выбрана категория <b>Даром</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/otdam-darom'
        queue.put(search_link)
    
    elif query.data == 'barter':
        query.message.edit_text(
            text='Выбрана категория <b>Обмен</b>',
            parse_mode=ParseMode.HTML,
            reply_markup = keyboards.backward
        )
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ищем что-то конкретное или отобразить все в этой категории?",
            reply_markup = keyboards.categories_choose
            )
        search_link = 'https://www.olx.ua/obmen-barter'
        queue.put(search_link)
    
    
    global j
    j=1

    return SEARCHCONTEXT


def searchcontext(update,context):
    query = update.callback_query
    if query.data == 'adverts':
        query.edit_message_text(
            text = 'Вы можете просто ввести поисковый запрос или \
            выбрать категорию в которой будет проводиться поиск',
            reply_markup = keyboards.categories_keyboard 
        )
        return SEARCHTEXT

    if query.data == 'categories':
        query.edit_message_text(
             
            text = "Выберите категорию для поиска",
            reply_markup = keyboards.categories_keyboard
          )    
        return CATEGORIES


def searchtext(update,context):
    global search_text
    search_text = update.message.text

    context.bot.send_message(
    chat_id = update.effective_chat.id,
    text =f'Собрать обьявления по запросу: <b>"{search_text}"</b>, верно?',
    reply_markup = keyboards.search_keyboard, 
    parse_mode = ParseMode.HTML 
    )
    
    return COLADV


def colect_categorie(update,context):
    chat_id = update.effective_chat.id
    search_link = queue.get()
    
    if search_link:
        get_web.get_adverts(f'{search_link}/', chat_id)
    
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f"<b>Обьявления собраны.</b> Вывести на экран?", 
        reply_markup=keyboards.colect_keyboard, parse_mode=ParseMode.HTML
        )

    return SENDADV_PROKL


def colect_advert(update,context):
    chat_id = update.effective_chat.id
   
    if j == 1:
        search_link = queue.get()
        get_web.get_adverts(f'{search_link}/q-'+ search_text, chat_id)
        
    else:
        get_web.get_adverts(f'https://www.olx.ua/list/q-{search_text}', chat_id)
    
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f"<b>Обьявления собраны.</b> Вывести на экран?", 
        reply_markup=keyboards.colect_keyboard, parse_mode=ParseMode.HTML
        )

    return SENDADV_PROKL
   

def send_advert_prokl(update, context):

    chat_id = update.effective_chat.id

    reply_markup = InlineKeyboardMarkup(keyboards.page_kayboard)

    with open(f'{chat_id}.txt', 'r', encoding='utf-8') as file:
            adverts = json.load(file)
        
    single_adv=adverts[0]
   
    text = """
<b>{title}</b>  
<i>Цена:</i> <b>{price}</b>
<i>Город:</i> <b>{location}</b> 
{url}


  <b>Для повторного поиска просто введите запрос</b>

""".format(**single_adv)

    context.bot.send_photo(
        chat_id = update.effective_chat.id,
        caption = f"  Вот что мне удалось найти, {text}  ", 
        parse_mode=ParseMode.HTML,
        reply_markup = reply_markup,
        photo = single_adv['img']
        )


    global i
    i=i+1
    
    return SENDADV


def send_advert(update, context):
        
    query = update.callback_query
    
    reply_markup = InlineKeyboardMarkup(keyboards.page_kayboard)
    
    global i
   
    try:
        chat_id = update.effective_chat.id
        with open(f'{chat_id}.txt', 'r', encoding='utf-8') as file:
            adverts = json.load(file)

        if query.data == '0' and i>0:

            i=i-1

            single_adv=adverts[i]
            print(single_adv)
        
        
            text = """
<b>{title}</b>  
<i>Цена:</i> <b>{price}</b>
<i>Город:</i> <b>{location}</b> 
{url}


<b>Для повторного поиска просто введите запрос</b>

""".format(**single_adv)

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
{url}


<b>Для повторного поиска просто введите запрос</b>

""".format(**single_adv)
        
            query.message.edit_media(
                media = InputMediaPhoto(
                    media = single_adv['img'],
                    caption=text,
                    parse_mode=ParseMode.HTML
                    ), 
                reply_markup=reply_markup)

            query.answer()
        
            if i == (len(adverts)-1):
                global page_counter
                page_counter = page_counter+1
                changer = str(single_adv['link'])
                if page_counter == 2:  
                    get_web.get_adverts(f"{changer}/?page={page_counter}", chat_id)
                    
                elif page_counter >2:
                    changer = changer[:-8]
                    print('re',changer)
                    get_web.get_adverts(f"{changer}/?page={page_counter}", chat_id)
                with open(f'{chat_id}.txt', 'r', encoding='utf-8') as file:
                     adverts = json.load(file)
              
                i = 0
               


          

        
    except telegram.error.BadRequest:

        single_adv=adverts[i]
        text = """
<b>{title}</b>  
<i>Цена:</i> <b>{price}</b>
<i>Город:</i> <b>{location}</b> 
{url}


<b>Для повторного поиска просто введите запрос</b>

""".format(**single_adv)
        
        query.message.edit_media(
            media = InputMediaPhoto(
                media = "https://retinaks.ru/files/default_images/nofoto.png",
                caption = text,
                parse_mode=ParseMode.HTML
                ),
            reply_markup=reply_markup
            )
        
        query.answer()

   
    except IndexError:
        
        query.message.edit_media(
            media = InputMediaPhoto(
            media = "https://retinaks.ru/files/default_images/nofoto.png",
            caption = f"Это все обьявления по запросу {search_text},\
                для повторного поиска просто введите запрос",
            parse_mode=ParseMode.HTML
            ),
        reply_markup=reply_markup
            )

        query.answer()


        if query.data == '0':
            
            i = i-1
            
            single_adv=adverts[i]
        
            text = """
<b>{title}</b>  
<i>Цена:</i> <b>{price}</b>
<i>Город:</i> <b>{location}</b> 
{url}


<b>Для повторного поиска просто введите запрос</b>

""".format(**single_adv)

            query.message.edit_media(
                media = InputMediaPhoto(
                    media = single_adv['img'],
                    caption=text,
                    parse_mode=ParseMode.HTML
                    ),
                reply_markup=reply_markup
                )
            
            query.answer()

           


            


def create_db(update,context):

   context.bot.send_message(
       chat_id = update.effective_chat.id,
       text = "Cобрать полученные результаты в файл?",
       reply_markup = keyboards.create_db_keyboard
       )
   
   return MAKEDB


def make_db(update,context):
    
    chat_id = update.effective_chat.id
    adverts = open(f'{chat_id}.txt', 'r', encoding='utf-8') 

    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f"Вот что мне удалось найти по запросу {search_text}"
    )
    context.bot.send_document(
        chat_id = update.effective_chat.id,
        document = adverts,
        filename = f'{search_text}',
        )



search = ConversationHandler(

    entry_points = [CommandHandler('start',start)],
    states ={
        SEARCHCONTEXT:[
            CallbackQueryHandler(searchcontext),
            MessageHandler(Filters.regex('^Поиск по категории$'),categories_start), 
            MessageHandler(Filters.regex('^Отобразить категорию$'), colect_categorie)
            ],

        CATEGORIES: [CallbackQueryHandler(categories)],

        SEARCHTEXT:[MessageHandler(Filters.text,searchtext)],

        COLADV: [
            MessageHandler(Filters.regex('^Все верно$'),colect_advert),
            ],

        SENDADV_PROKL: [
            MessageHandler(Filters.regex('^Да, покажи$'),send_advert_prokl),
            MessageHandler(Filters.regex('^Сохрани в базу данных$'),create_db)
        ],

        SENDADV:[
            
            CallbackQueryHandler(send_advert) 
            ],

        MAKEDB: [MessageHandler(Filters.regex('^Да, собери$'),make_db)],

        
    },
    fallbacks = [
        MessageHandler(Filters.regex('^Изменить запрос$') | Filters.command,start),
        MessageHandler(Filters.regex('^Найди еще$'),start),
        MessageHandler(Filters.text,searchtext)
        
        ]
)