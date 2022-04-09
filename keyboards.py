from telegram import  ParseMode, InlineKeyboardMarkup, replymarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


PREV,NEXT = range(2)
i=0



categories = [ 
       [ 
            InlineKeyboardButton("Дети", callback_data='child'),
            InlineKeyboardButton("Недвижимость", callback_data='estate'),
            InlineKeyboardButton("Авто", callback_data='auto')
        ],
        [
            InlineKeyboardButton("Запчасти", callback_data='parts'),
            InlineKeyboardButton("Работа", callback_data='job'),
            InlineKeyboardButton("Животные", callback_data='animals')
        ],
        [
            InlineKeyboardButton("Для дома", callback_data='house'),
            InlineKeyboardButton("Техника", callback_data='elect'),
            InlineKeyboardButton("Услуги", callback_data='service')
        ],
        [
            InlineKeyboardButton("Мода и стиль", callback_data='fashion'),
            InlineKeyboardButton("Хобби", callback_data='hobby'),
            InlineKeyboardButton("Даром", callback_data='free'),
            InlineKeyboardButton("Обмен", callback_data='barter')
        ],
        [
            InlineKeyboardButton("Назад", callback_data='back')
        ]
   ]

categories_keyboard =  InlineKeyboardMarkup(categories)


categories_child_first = [
        [   
            InlineKeyboardButton("Показать все", callback_data='child all')
        ],
        [ 
            InlineKeyboardButton("Одежда", callback_data='child clothes'),
            InlineKeyboardButton("Обувь", callback_data='child shoes'),
            InlineKeyboardButton("Коляски", callback_data='child wagon')
        ],
        [
            InlineKeyboardButton("Мебель", callback_data='child furniture'),
            InlineKeyboardButton("Игрушки", callback_data='toys'),
            InlineKeyboardButton("Транспорт", callback_data='child transport')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='child more'),
        ],
            [InlineKeyboardButton("Все категории", callback_data='back')]
    ]

child_first_keyboard = InlineKeyboardMarkup(categories_child_first)

categories_child_second = [
        
        [
            InlineKeyboardButton("Кормление", callback_data='feeding'),
            InlineKeyboardButton("Школа", callback_data='school'),
            InlineKeyboardButton("Автокресла", callback_data='carchair')
        ],
        [
         InlineKeyboardButton("Прочее", callback_data='child other')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='child less')
        ],
        [   
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]
    

child_second_keyboard = InlineKeyboardMarkup(categories_child_second)


categories_estate = [
        [   
            InlineKeyboardButton("Показать все", callback_data='estate all')
        ],
        [ 
            InlineKeyboardButton("Квартиры", callback_data='apartment'),
            InlineKeyboardButton("Комнаты", callback_data='room'),
            InlineKeyboardButton("Дома", callback_data='house')
        ],
        [
            InlineKeyboardButton("Земля", callback_data='land'),
            InlineKeyboardButton("Комерческая", callback_data='comercial'),
            InlineKeyboardButton("Гаражи", callback_data='garage')
        ],
        [
            InlineKeyboardButton("Посуточно", callback_data='rent'),
            InlineKeyboardButton("За рубежом", callback_data='foreign')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]     
    ]

estate_keyboard = InlineKeyboardMarkup(categories_estate)


categories_auto_first = [
        [   
            InlineKeyboardButton("Показать все", callback_data='auto all')
        ],
        [ 
            InlineKeyboardButton("Легковые", callback_data='legkovie'),
            InlineKeyboardButton("Автобусы", callback_data='bus'),
            InlineKeyboardButton("Водный", callback_data='aqua')
        ],
        [
            InlineKeyboardButton("Из Польши", callback_data='poland'),
            InlineKeyboardButton("Мото", callback_data='moto'),
            InlineKeyboardButton("Воздушный транспорт", callback_data='air')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='auto more'),
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

auto_first_keyboard = InlineKeyboardMarkup(categories_auto_first)


categories_auto_second = [
        [
            InlineKeyboardButton("Показать все", callback_data='auto all')
        ],
        [ 
            InlineKeyboardButton("Запчасти", callback_data='auto parts'),
            InlineKeyboardButton("Нерастаможеные", callback_data='tamog'),
            InlineKeyboardButton("Грузовые", callback_data='gruz')
        ],
        [
            InlineKeyboardButton("Спецтехника", callback_data='special'),
            InlineKeyboardButton("Прицепы", callback_data='pricep'),
            InlineKeyboardButton("Электротранспорт", callback_data='electro')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='auto less')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

auto_second_keyboard = InlineKeyboardMarkup(categories_auto_second)


categories_parts = [
        [
            InlineKeyboardButton("Показать все", callback_data='parts all')
        ],
        [ 
            InlineKeyboardButton("Автозапчасти", callback_data='auto parts'),
            InlineKeyboardButton("Шины, диски...", callback_data='weels'),
            InlineKeyboardButton("Для спец.техники", callback_data='parts special')
        ],
        [
            InlineKeyboardButton("Мотозапчасти", callback_data='moto parts'),
            InlineKeyboardButton("Прочее", callback_data='parts else'),
            InlineKeyboardButton("Авто", callback_data='parts auto')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

parts_keyboard = InlineKeyboardMarkup(categories_parts)


categories_animals_first = [
        [
            InlineKeyboardButton("Показать все", callback_data='animals all')
        ],
        [ 
            InlineKeyboardButton("Бесплатно", callback_data='animals free'),
            InlineKeyboardButton("Собаки", callback_data='dogs'),
            InlineKeyboardButton("Кошки", callback_data='cats')
        ],
        [
            InlineKeyboardButton("Аквариумистика", callback_data='auqariums'),
            InlineKeyboardButton("Птицы", callback_data='birds'),
            InlineKeyboardButton("Грызуны", callback_data='rats')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='animals more')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

animals_first_keyboard = InlineKeyboardMarkup(categories_animals_first)

categories_animals_second = [
        [
            InlineKeyboardButton("Показать все", callback_data='animals all')
        ],
        [ 
            InlineKeyboardButton("Рептилии", callback_data='reptiles'),
            InlineKeyboardButton("Сельхоз животные", callback_data='farm'),
            InlineKeyboardButton("Другие", callback_data='animals else')
        ],
        [
            InlineKeyboardButton("Зоотовары", callback_data='animals feed'),
            InlineKeyboardButton("Вязка", callback_data='breed'),
            InlineKeyboardButton("Бюро находок", callback_data='found')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='animals less')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

animals_second_keyboard = InlineKeyboardMarkup(categories_animals_second)


categories_house_first = [
        [
            InlineKeyboardButton("Показать все", callback_data='house all')
        ],
        [ 
            InlineKeyboardButton("Канцтовары", callback_data='kanz'),
            InlineKeyboardButton("Мебель", callback_data='furniture'),
            InlineKeyboardButton("Продукты", callback_data='grocery')
        ],
        [
            InlineKeyboardButton("Сад/огород", callback_data='garden'),
            InlineKeyboardButton("Интерьер", callback_data='interier'),
            InlineKeyboardButton("Строительство", callback_data='building')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='house more')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

house_first_keyboard = InlineKeyboardMarkup(categories_house_first)

categories_house_second = [
        [
            InlineKeyboardButton("Показать все", callback_data='house all')
        ],
        [ 
            InlineKeyboardButton("Инструменты", callback_data='tools'),
            InlineKeyboardButton("Растения", callback_data='plants'),
            InlineKeyboardButton("Посуда", callback_data='dishes')
        ],
        [
            InlineKeyboardButton("Садовый инвентарь", callback_data='garden tools'),
            InlineKeyboardButton("Быт.Химия", callback_data='chemistry'),
            InlineKeyboardButton("Прочее", callback_data='house else')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='house less')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

house_second_keyboard = InlineKeyboardMarkup(categories_house_second)


categories_elect_first = [
        [
            InlineKeyboardButton("Показать все", callback_data='elect all')
        ],
        [ 
            InlineKeyboardButton("Телефоны", callback_data='phones'),
            InlineKeyboardButton("Компьютеры", callback_data='PC'),
            InlineKeyboardButton("Игры и приставки", callback_data='games')  
        ],
        [
            InlineKeyboardButton("ТВ", callback_data='TV'),
            InlineKeyboardButton("Аудиотехника", callback_data='audio'),
            InlineKeyboardButton("Ремонт", callback_data='repair')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='elect more')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

elect_first_keyboard = InlineKeyboardMarkup(categories_elect_first)

categories_elect_second = [
        [
            InlineKeyboardButton("Показать все", callback_data='elect all')
        ],
        [ 
            InlineKeyboardButton("Фото/видео", callback_data='photo'),
            InlineKeyboardButton("Планшеты", callback_data='plansh'),
            InlineKeyboardButton("Ноутбуки", callback_data='tablets'),
               
        ],
        [
            InlineKeyboardButton("Климатическое", callback_data='climat'),
            InlineKeyboardButton("Уход", callback_data='selfcare'),
            InlineKeyboardButton("Аксесуары", callback_data='acesoars')
        ],
        [
            InlineKeyboardButton("Для дома", callback_data='for home'),
            InlineKeyboardButton("Для кухни", callback_data='for kitchen'),
             InlineKeyboardButton("Прочее", callback_data='elect else')
        ],
        [
            InlineKeyboardButton("Еще", callback_data='elect less')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

elect_second_keyboard = InlineKeyboardMarkup(categories_elect_second)


categories_fasion = [
        [
            InlineKeyboardButton("Показать все", callback_data='fashion all')
        ],
        [ 
            InlineKeyboardButton("Одежда/обувь", callback_data='clothes'),
            InlineKeyboardButton("Для свадьбы", callback_data='wedding'),
            InlineKeyboardButton("Красота/здоровье", callback_data='beuty')
        ],
        [
            InlineKeyboardButton("Часы", callback_data='wathc'),
            InlineKeyboardButton("Аксессуары", callback_data='fashion acsesours'),
            InlineKeyboardButton("Подарки", callback_data='gifts')
        ],
        [
            InlineKeyboardButton("Прочее", callback_data='fashion else')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

fashion_keyboard = InlineKeyboardMarkup(categories_fasion)


categories_hobby = [
        [
            InlineKeyboardButton("Показать все", callback_data='hobby all')
        ],
        [ 
            InlineKeyboardButton("Антиквариат", callback_data='antiquary'),
            InlineKeyboardButton("Муз. инструменты", callback_data='guitars'),
            InlineKeyboardButton("Книги", callback_data='books')
        ],
        [ 
            InlineKeyboardButton("Спорт", callback_data='sport'),
            InlineKeyboardButton("CD/DVD/пластинки", callback_data='CD'),
            InlineKeyboardButton("Билеты", callback_data='tickets')
        ],
        [
            InlineKeyboardButton("Попутчики", callback_data='road'),
            InlineKeyboardButton("Музыканты", callback_data='musicians'),
            InlineKeyboardButton("Прочее", callback_data='hobby else')
        ],
        [
            InlineKeyboardButton("Все категории", callback_data='back')
        ]
    ]

hobby_keyboard = InlineKeyboardMarkup(categories_hobby)




page_kayboard = [
        [
            InlineKeyboardButton("Предыдущее обьявление", callback_data=str(PREV), i=i-1),
            InlineKeyboardButton("Следующее обьявление", callback_data=str(NEXT), i=i+1),
        ]
    ]
pages_kayboard = InlineKeyboardMarkup(page_kayboard )


start_keyboard = [
    [
        InlineKeyboardButton("Поиск по категории",callback_data = 'categories')
    ]
]

start_keyboard = InlineKeyboardMarkup(start_keyboard)


ok_keyboard = [
    [
        InlineKeyboardButton("Верно",callback_data = 'Ok'),
    ],
    [
        InlineKeyboardButton("Назад", callback_data='back')
    ]
]

ok_keyboard=InlineKeyboardMarkup(ok_keyboard)


search_keyboard = ReplyKeyboardMarkup(
        [['Все верно'],["Изменить запрос"]],
        one_time_keyboard=True,
        resize_keyboard=True
        )



colect_keyboard = ReplyKeyboardMarkup(
        [['Да, покажи'],['Сохрани в базу данных'],["Изменить запрос"]],
        one_time_keyboard=True,
        resize_keyboard=True
        )

create_db_keyboard = ReplyKeyboardMarkup(
       [['Да, собери'],["Изменить запрос"]],
       one_time_keyboard=True,
       resize_keyboard=True
       )

categories_choose = ReplyKeyboardMarkup([['Ввести запрос'],['Отобразить категорию']],
        one_time_keyboard=True,
        resize_keyboard=True)


        