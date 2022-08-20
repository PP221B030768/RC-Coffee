import telebot
from telebot import types
import random

bot = telebot.TeleBot('5483436479:AAFk1sCPduS9nz_kQ3eulVNuPqv7U89CY90')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name != None:
        mess_start = f'<b>{message.from_user.first_name} {message.from_user.last_name}</b>, рады Вас приветствовать!'
    else:
        mess_start = f'<b>{message.from_user.first_name}</b>, рады Вас приветствовать!'
    bot.send_message(message.chat.id, mess_start, parse_mode='html')

    mess_1 = 'Я - Ваш виртуальный ассистент из кофейни RC Coffee. Не можешь определиться с выбором напитка и десерта? Я тебе помогу!'
    keyboard = types.InlineKeyboardMarkup()
    key_continue = types.InlineKeyboardButton(text='Продолжить', callback_data='continue')
    keyboard.add(key_continue)
    bot.send_message(message.from_user.id, text=mess_1, reply_markup=keyboard)

@bot.message_handler(commands=["media"])
# def cmd_start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton(text="Instagram", url="https://github.com")
#     item2 = types.KeyboardButton("Wolt")
#     markup.add(item1, item2)
#     bot.send_message(message.chat.id, 'Мы в соц сетях:', parse_mode='html', reply_markup=markup)
def cmd_inline_url(message):
    buttons = [
        types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/rc_coffee_kst/"),
        types.InlineKeyboardButton(text="Wolt (Mart)", url="https://wolt.com/ru/kaz/kostanay/restaurant/rc-coffee-mart"),
        types.InlineKeyboardButton(text="Wolt (Plaza)", url="https://wolt.com/kk/kaz/kostanay/restaurant/rc-coffee-plaza"),
        types.InlineKeyboardButton(text="2gis", url="https://2gis.kz/kostanay/branches/70000001035191880")
    ]
    keyboard000 = types.InlineKeyboardMarkup(row_width=1)
    keyboard000.add(*buttons)
    bot.send_message(message.chat.id, 'Мы в соц сетях:', parse_mode='html', reply_markup=keyboard000)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    s = ""

    bot.answer_callback_query(callback_query_id=call.id, text='Хорошо!')

    keyboard0 = types.InlineKeyboardMarkup(row_width=1)
    key_mart = types.InlineKeyboardButton(text='ТРЦ Март', callback_data='mart')
    key_plaza = types.InlineKeyboardButton(text='ТРЦ Костанай Плаза', callback_data='plaza')
    keyboard0.add(key_mart, key_plaza)
    if call.data == 'continue':
        bot.send_message(call.message.chat.id, text='В каком филиале ты находишься?', reply_markup=keyboard0)

    keyboard00 = types.InlineKeyboardMarkup(row_width=2)
    key_drinks = types.InlineKeyboardButton(text='Напитки', callback_data='drinks')
    key_desert = types.InlineKeyboardButton(text='Десерты', callback_data='desert')
    keyboard00.add(key_drinks, key_desert)
    if call.data == 'mart' or call.data == 'plaza':
        bot.send_message(call.message.chat.id, text='С чего начнем?', reply_markup=keyboard00)

    keyboard1 = types.InlineKeyboardMarkup(row_width=1)
    key_cold = types.InlineKeyboardButton(text='Холодный кофе', callback_data='cold')
    key_hot = types.InlineKeyboardButton(text='Горячие напитки', callback_data='hot')
    key_refreshing = types.InlineKeyboardButton(text='Напитки', callback_data='drink')
    keyboard1.add(key_cold, key_hot, key_refreshing)
    if call.data == 'drinks':
        bot.send_message(call.message.chat.id, text='Давай выберем напиток:', reply_markup=keyboard1)


    keyboard2 = types.InlineKeyboardMarkup(row_width=1)
    key_americano = types.InlineKeyboardButton(text='Американо ICE', callback_data='americano')
    key_mors = types.InlineKeyboardButton(text='Кофейный морс', callback_data='mors')
    key_latte = types.InlineKeyboardButton(text='Латте ICE', callback_data='latte')
    keyboard2.add(key_americano, key_mors, key_latte)
    if call.data == 'cold':
        bot.send_message(call.message.chat.id, text='Теперь осталось определиться с видом холодного кофе:', reply_markup=keyboard2)

    keyboard3 = types.InlineKeyboardMarkup(row_width=1)
    key_author_coffee = types.InlineKeyboardButton(text='Авторский кофе', callback_data='author_coffee')
    key_classic_coffee = types.InlineKeyboardButton(text='Классический кофе', callback_data='classic_coffee')
    key_author_tea = types.InlineKeyboardButton(text='Авторский чай', callback_data='author_tea')
    key_classic_tea = types.InlineKeyboardButton(text='Классический чай', callback_data='classic_tea')
    keyboard3.add(key_author_coffee, key_classic_coffee, key_author_tea, key_classic_tea)
    if call.data == 'hot':
        bot.send_message(call.message.chat.id, text='Выбор непростой, но я обязательно помогу!')
        bot.send_message(call.message.chat.id, text='К классическому кофе относятся самые стандартные рецепты кофе: эспрессо, латте и т.д. Аналогично и с классическим чаем. Например, зеленый чай, имбирный и т.д.')
        mess_start = 'Авторский кофе, как и чай, - немного необычный по вкусу. Готовятся с добавлением различных сиропов и топингов, а также, пряностей.'
        bot.send_message(call.message.chat.id, text=mess_start, reply_markup=keyboard3, parse_mode='html')

    keyboard4 = types.InlineKeyboardMarkup(row_width=1)
    key_water = types.InlineKeyboardButton(text='Bonaqua, 500 мл', callback_data='water')
    key_piko_peach = types.InlineKeyboardButton(text='Piko Персик, 200 мл', callback_data='piko_peach')
    key_piko_apple = types.InlineKeyboardButton(text='Piko Яблоко, 200 мл', callback_data='piko_apple')
    keyboard4.add(key_water, key_piko_peach, key_piko_apple)
    if call.data == 'drink':
        bot.send_message(call.message.chat.id, 'Здесь все просто:', reply_markup=keyboard4, parse_mode='html')

    keyboard19 = types.InlineKeyboardMarkup()
    key_yes0 = types.InlineKeyboardButton(text='Да', callback_data='yes0')
    key_no0 = types.InlineKeyboardButton(text='Нет', callback_data='no0')
    keyboard19.add(key_yes0, key_no0)

    keyboard100 = types.InlineKeyboardMarkup()
    key_300_0 = types.InlineKeyboardButton(text='300 мл', callback_data='300_0')
    key_400_0 = types.InlineKeyboardButton(text='400 мл', callback_data='400_0')
    key_500_0 = types.InlineKeyboardButton(text='500 мл', callback_data='500_0')
    keyboard100.add(key_300_0, key_400_0, key_500_0)

    if call.data == 'americano':
        bot.send_message(call.message.chat.id, text='Американо ICE - классический холодный американо')
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='300 мл - 900 тг, 400 мл - 1000 тг, 500 мл - 1100 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard19)

    if call.data == 'yes0':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard100)

    if call.data == '300_0':
        s =  s + " " + "Американо ICE" + " " + '300 мл'
        print(s)

    if call.data == '400_0':
        s =  s + " " + "Американо ICE" + " " + '400 мл'
        print(s)

    if call.data == '500_0':
        s =  s + " " + "Американо ICE" + " " + '500 мл'
        print(s)

    keyboard20 = types.InlineKeyboardMarkup()
    key_yes1 = types.InlineKeyboardButton(text='Да', callback_data='yes1')
    key_no1 = types.InlineKeyboardButton(text='Нет', callback_data='no1')
    keyboard20.add(key_yes1, key_no1)

    keyboard101 = types.InlineKeyboardMarkup()
    key_300_1 = types.InlineKeyboardButton(text='300 мл', callback_data='300_1')
    key_400_1 = types.InlineKeyboardButton(text='400 мл', callback_data='400_1')
    key_500_1 = types.InlineKeyboardButton(text='500 мл', callback_data='500_1')
    keyboard101.add(key_300_1, key_400_1, key_500_1)

    if call.data == 'mors':
        bot.send_message(call.message.chat.id, text='Кофейный морс - кофейный холодный напиток с добавлением апельсинового/вишневого сока')
        bot.send_message(call.message.chat.id, text='300 мл - 1100 тг, 400 мл - 1200 тг, 500 мл - 1300 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard20)

    if call.data == 'yes1':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard101)


    if call.data == '300_1':
        s =  s + " " + "Кофейный морс" + " " + '300 мл'
        print(s)

    if call.data == '400_1':
        s =  s + " " + "Кофейный морс" + " " + '400 мл'
        print(s)

    if call.data == '500_1':
        s =  s + " " + "Кофейный морс" + " " + '500 мл'
        print(s)

    keyboard21 = types.InlineKeyboardMarkup()
    key_yes2 = types.InlineKeyboardButton(text='Да', callback_data='yes2')
    key_no2 = types.InlineKeyboardButton(text='Нет', callback_data='no2')
    keyboard21.add(key_yes2, key_no2)

    keyboard102 = types.InlineKeyboardMarkup()
    key_300_2 = types.InlineKeyboardButton(text='300 мл', callback_data='300_2')
    key_400_2 = types.InlineKeyboardButton(text='400 мл', callback_data='400_2')
    key_500_2 = types.InlineKeyboardButton(text='500 мл', callback_data='500_2')
    keyboard102.add(key_300_2, key_400_2, key_500_2)

    if call.data == 'latte':
        bot.send_message(call.message.chat.id, text='Латте ICE - классический холодный латте')
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='300 мл - 1000 тг, 400 мл - 1100 тг, 500 мл - 1200 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard21)

    if call.data == 'yes2':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard102)

    if call.data == '300_2':
        s =  s + " " + "Латте ICE" + " " + '300 мл'
        print(s)

    if call.data == '400_2':
        s =  s + " " + "Латте ICE" + " " + '400 мл'
        print(s)

    if call.data == '500_2':
        s =  s + " " + "Латте ICE" + " " + '500 мл'
        print(s)


    keyboard7 = types.InlineKeyboardMarkup(row_width=1)
    key_nut = types.InlineKeyboardButton(text='Король орех', callback_data='nut')
    key_halva = types.InlineKeyboardButton(text='Кофе с халвой', callback_data='halva')
    key_almond = types.InlineKeyboardButton(text='Миндальный бум', callback_data='almond')
    key_raf = types.InlineKeyboardButton(text='Рафаэлло', callback_data='raf')
    key_salt_latte = types.InlineKeyboardButton(text='Солёный латте XXL', callback_data='salt_latte')
    key_firm = types.InlineKeyboardButton(text='Фирменный кофе RC COFFEE', callback_data='firm')
    keyboard7.add(key_nut, key_halva, key_almond, key_raf, key_salt_latte, key_firm)
    if call.data == 'author_coffee':
        bot.send_message(call.message.chat.id, 'Перед тобой список авторского кофе', reply_markup=keyboard7, parse_mode='html')

    keyboard8 = types.InlineKeyboardMarkup(row_width=1)
    key_amer = types.InlineKeyboardButton(text='Американо', callback_data='amer')
    key_cap = types.InlineKeyboardButton(text='Капучино', callback_data='cap')
    key_lat = types.InlineKeyboardButton(text='Латте', callback_data='lat')
    key_mok = types.InlineKeyboardButton(text='Мокачино', callback_data='mok')
    key_flat = types.InlineKeyboardButton(text='Флэт уайт', callback_data='flat')
    key_kakao = types.InlineKeyboardButton(text='Какао', callback_data='kakao')
    key_chok = types.InlineKeyboardButton(text='Горячий шоколад', callback_data='chok')
    keyboard8.add(key_amer, key_cap, key_lat, key_mok, key_flat, key_kakao, key_chok)
    if call.data == 'classic_coffee':
        bot.send_message(call.message.chat.id, 'Перед тобой список классического кофе', reply_markup=keyboard8, parse_mode='html')

    keyboard9 = types.InlineKeyboardMarkup(row_width=1)
    keyboard9.add(key_amer, key_cap, key_lat, key_mok, key_flat, key_kakao, key_chok)

    keyboard22 = types.InlineKeyboardMarkup()
    key_yes3 = types.InlineKeyboardButton(text='Да', callback_data='yes3')
    key_no3 = types.InlineKeyboardButton(text='Нет', callback_data='no3')
    keyboard22.add(key_yes3, key_no3)

    keyboard103 = types.InlineKeyboardMarkup()
    key_250_3 = types.InlineKeyboardButton(text='250 мл', callback_data='250_3')
    key_350_3 = types.InlineKeyboardButton(text='350 мл', callback_data='350_3')
    key_450_3 = types.InlineKeyboardButton(text='450 мл', callback_data='450_3')
    keyboard103.add(key_250_3, key_350_3, key_450_3)

    if call.data == 'amer':
        txt1 = 'Напиток на основе эспрессо, дополнительно разбавленный водой. Вкус правильного американо – нерезкий, деликатный, без горького привкуса, менее крепкий и более мягкий, чем у обычного эспрессо.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 750 тг, 350 мл - 850 тг, 450 мл - 950 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard22)

    if call.data == 'yes3':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard103)

    if call.data == '250_3':
        s =  s + " " + "Американо" + " " + '250 мл'
        print(s)

    if call.data == '350_3':
        s =  s + " " + "Американо" + " " + '350 мл'
        print(s)

    if call.data == '450_3':
        s =  s + " " + "Американо" + " " + '450 мл'
        print(s)

    keyboard23 = types.InlineKeyboardMarkup()
    key_yes4 = types.InlineKeyboardButton(text='Да', callback_data='yes4')
    key_no4 = types.InlineKeyboardButton(text='Нет', callback_data='no4')
    keyboard23.add(key_yes4, key_no4)

    keyboard104 = types.InlineKeyboardMarkup()
    key_250_4 = types.InlineKeyboardButton(text='250 мл', callback_data='250_4')
    key_350_4 = types.InlineKeyboardButton(text='350 мл', callback_data='350_4')
    key_450_4 = types.InlineKeyboardButton(text='450 мл', callback_data='450_4')
    keyboard104.add(key_250_4, key_350_4, key_450_4)

    if call.data == 'cap':
        txt1 = 'Кофейный напиток итальянской кухни на основе эспрессо с добавлением в него подогретого вспененного молока.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 900 тг, 350 мл - 1000 тг, 450 мл - 1100 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard23)

    if call.data == 'yes4':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard104)

    if call.data == '250_4':
        s =  s + " " + "Капучино" + " " + '250 мл'
        print(s)

    if call.data == '350_4':
        s =  s + " " + "Капучино" + " " + '350 мл'
        print(s)

    if call.data == '450_4':
        s =  s + " " + "Капучино" + " " + '450 мл'
        print(s)

    keyboard24 = types.InlineKeyboardMarkup()
    key_yes5 = types.InlineKeyboardButton(text='Да', callback_data='yes5')
    key_no5 = types.InlineKeyboardButton(text='Нет', callback_data='no5')
    keyboard24.add(key_yes5, key_no5)

    keyboard105 = types.InlineKeyboardMarkup()
    key_250_5 = types.InlineKeyboardButton(text='250 мл', callback_data='250_5')
    key_350_5 = types.InlineKeyboardButton(text='350 мл', callback_data='350_5')
    key_450_5 = types.InlineKeyboardButton(text='450 мл', callback_data='450_5')
    keyboard105.add(key_250_5, key_350_5, key_450_5)

    if call.data == 'lat':
        txt1 = 'Латте (он же латте-макиато) — это молочный напиток на основе кофе эспрессо. Готовится при помощи вспененного молока и состоит из трех слоев: молока, кофе и молочной пенки. Он обладает нежным молочным вкусом.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 900 тг, 350 мл - 1000 тг, 450 мл - 1100 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard24)

    if call.data == 'yes5':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard105)

    if call.data == '250_5':
        s =  s + " " + "Латте" + " " + '250 мл'
        print(s)

    if call.data == '350_5':
        s =  s + " " + "Латте" + " " + '350 мл'
        print(s)

    if call.data == '450_5':
        s =  s + " " + "Латте" + " " + '450 мл'
        print(s)

    keyboard25 = types.InlineKeyboardMarkup()
    key_yes6 = types.InlineKeyboardButton(text='Да', callback_data='yes6')
    key_no6 = types.InlineKeyboardButton(text='Нет', callback_data='no6')
    keyboard25.add(key_yes6, key_no6)

    keyboard106 = types.InlineKeyboardMarkup()
    key_250_6 = types.InlineKeyboardButton(text='250 мл', callback_data='250_6')
    key_350_6 = types.InlineKeyboardButton(text='350 мл', callback_data='350_6')
    key_450_6 = types.InlineKeyboardButton(text='450 мл', callback_data='450_6')
    keyboard106.add(key_250_6, key_350_6, key_450_6)

    if call.data == 'mok':
        txt1 = 'Кофейный напиток, созданный в Америке и являющийся разновидностью латте с добавлением какао.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 950 тг, 350 мл - 1050 тг, 450 мл - 1150 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard25)

    if call.data == 'yes6':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard106)

    if call.data == '250_6':
        s =  s + " " + "Мокачино" + " " + '250 мл'
        print(s)

    if call.data == '350_6':
        s =  s + " " + "Мокачино" + " " + '350 мл'
        print(s)

    if call.data == '450_6':
        s =  s + " " + "Мокачино" + " " + '450 мл'
        print(s)

    keyboard26 = types.InlineKeyboardMarkup()
    key_yes7 = types.InlineKeyboardButton(text='Да', callback_data='yes7')
    key_no7 = types.InlineKeyboardButton(text='Нет', callback_data='no7')
    keyboard26.add(key_yes7, key_no7)

    if call.data == 'flat':
        txt1 = 'Напиток с бархатистой нежной текстурой и ярко выраженным кофейным вкусом.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard26)

    if call.data == 'yes7':
        s =  s + " " + "Флэт уайт" + " " + '250 мл'
        print(s)

    keyboard27 = types.InlineKeyboardMarkup()
    key_yes8 = types.InlineKeyboardButton(text='Да', callback_data='yes8')
    key_no8 = types.InlineKeyboardButton(text='Нет', callback_data='no8')
    keyboard27.add(key_yes8, key_no8)

    keyboard108 = types.InlineKeyboardMarkup()
    key_250_8 = types.InlineKeyboardButton(text='250 мл', callback_data='250_8')
    key_350_8 = types.InlineKeyboardButton(text='350 мл', callback_data='350_8')
    key_450_8 = types.InlineKeyboardButton(text='450 мл', callback_data='450_8')
    keyboard108.add(key_250_8, key_350_8, key_450_8)

    if call.data == 'kakao':
        txt1 = 'Какао — напиток, в состав которого обязательно входит какао, а также молоко (или вода) и сахар.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 800 тг, 350 мл - 850 тг, 450 мл - 900 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard27)

    if call.data == 'yes8':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard108)

    if call.data == '250_8':
        s =  s + " " + "Какао" + " " + '250 мл'
        print(s)

    if call.data == '350_8':
        s =  s + " " + "Какао" + " " + '350 мл'
        print(s)

    if call.data == '450_8':
        s =  s + " " + "Какао" + " " + '450 мл'
        print(s)

    keyboard28 = types.InlineKeyboardMarkup()
    key_yes9 = types.InlineKeyboardButton(text='Да', callback_data='yes9')
    key_no9 = types.InlineKeyboardButton(text='Нет', callback_data='no9')
    keyboard28.add(key_yes9, key_no9)

    keyboard109 = types.InlineKeyboardMarkup()
    key_250_9 = types.InlineKeyboardButton(text='250 мл', callback_data='250_9')
    key_350_9 = types.InlineKeyboardButton(text='350 мл', callback_data='350_9')
    key_450_9 = types.InlineKeyboardButton(text='450 мл', callback_data='450_9')
    keyboard109.add(key_250_9, key_350_9, key_450_9)

    if call.data == 'chok':
        txt1 = 'Горячим шоколадом называют напиток, приготовленный на основе какао с добавлением молока и сахара.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1100 тг, 450 мл - 1200 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard28)

    if call.data == 'yes9':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard109)

    if call.data == '250_9':
        s =  s + " " + "Горячий шоколад" + " " + '250 мл'
        print(s)

    if call.data == '350_9':
        s =  s + " " + "Горячий шоколад" + " " + '350 мл'
        print(s)

    if call.data == '450_9':
        s =  s + " " + "Горячий шоколад" + " " + '450 мл'
        print(s)

    keyboard29 = types.InlineKeyboardMarkup()
    key_yes10 = types.InlineKeyboardButton(text='Да', callback_data='yes10')
    key_no10 = types.InlineKeyboardButton(text='Нет', callback_data='no10')
    keyboard29.add(key_yes10, key_no10)

    if call.data == 'water':
        bot.send_message(call.message.chat.id, text='270 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard29)

    if call.data == 'yes10':
        s =  s + " " + "Вода Bonaqua, 500 мл" + " " 
        print(s)

    keyboard30 = types.InlineKeyboardMarkup()
    key_yes11 = types.InlineKeyboardButton(text='Да', callback_data='yes11')
    key_no11 = types.InlineKeyboardButton(text='Нет', callback_data='no11')
    keyboard30.add(key_yes11, key_no11)

    if call.data == 'piko_peach':
        bot.send_message(call.message.chat.id, text='300 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard30)

    if call.data == 'yes11':
        s =  s + " " + "Piko Персик, 250 мл" + " " 
        print(s)

    keyboard31 = types.InlineKeyboardMarkup()
    key_yes12 = types.InlineKeyboardButton(text='Да', callback_data='yes12')
    key_no12 = types.InlineKeyboardButton(text='Нет', callback_data='no12')
    keyboard31.add(key_yes12, key_no12)

    if call.data == 'piko_apple':
        bot.send_message(call.message.chat.id, text='300 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard31)

    if call.data == 'yes12':
        s =  s + " " + "Piko Яблоко, 250 мл" + " " 
        print(s)

    keyboard33 = types.InlineKeyboardMarkup()
    key_yes33 = types.InlineKeyboardButton(text='Да', callback_data='yes33')
    key_no33 = types.InlineKeyboardButton(text='Нет', callback_data='no33')
    keyboard33.add(key_yes33, key_no33)

    keyboard133 = types.InlineKeyboardMarkup()
    key_250_33 = types.InlineKeyboardButton(text='250 мл', callback_data='250_33')
    key_350_33 = types.InlineKeyboardButton(text='350 мл', callback_data='350_33')
    key_450_33 = types.InlineKeyboardButton(text='450 мл', callback_data='450_33')
    keyboard133.add(key_250_33, key_350_33, key_450_33)

    if call.data == 'nut':
        txt1 = 'Кофейный напиток с добавлением арахисовой пасты и шоколадного сиропа.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1200 тг, 450 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard33)

    if call.data == 'yes33':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard133)

    if call.data == '250_33':
        s =  s + " " + "Король орех" + " " + '250 мл'
        print(s)

    if call.data == '350_33':
        s =  s + " " + "Король орех" + " " + '350 мл'
        print(s)

    if call.data == '450_33':
        s =  s + " " + "Король орех" + " " + '450 мл'
        print(s)

    keyboard34 = types.InlineKeyboardMarkup()
    key_yes34 = types.InlineKeyboardButton(text='Да', callback_data='yes34')
    key_no34 = types.InlineKeyboardButton(text='Нет', callback_data='no34')
    keyboard34.add(key_yes34, key_no34)

    keyboard134 = types.InlineKeyboardMarkup()
    key_250_34 = types.InlineKeyboardButton(text='250 мл', callback_data='250_34')
    key_350_34 = types.InlineKeyboardButton(text='350 мл', callback_data='350_34')
    key_450_34 = types.InlineKeyboardButton(text='450 мл', callback_data='450_34')
    keyboard134.add(key_250_34, key_350_34, key_450_34)

    if call.data == 'halva':
        txt1 = 'Кофейный напиток с добавлением Халвы и сиропа со вкусом лесных орехов.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1200 тг, 450 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard34)

    if call.data == 'yes34':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard134)

    if call.data == '250_34':
        s =  s + " " + "Кофе с халвой" + " " + '250 мл'
        print(s)

    if call.data == '350_34':
        s =  s + " " + "Кофе с халвой" + " " + '350 мл'
        print(s)

    if call.data == '450_34':
        s =  s + " " + "Кофе с халвой" + " " + '450 мл'
        print(s)

    keyboard35 = types.InlineKeyboardMarkup()
    key_yes35 = types.InlineKeyboardButton(text='Да', callback_data='yes35')
    key_no35 = types.InlineKeyboardButton(text='Нет', callback_data='no35')
    keyboard35.add(key_yes35, key_no35)

    keyboard135 = types.InlineKeyboardMarkup()
    key_250_35 = types.InlineKeyboardButton(text='250 мл', callback_data='250_35')
    key_350_35 = types.InlineKeyboardButton(text='350 мл', callback_data='350_35')
    key_450_35 = types.InlineKeyboardButton(text='450 мл', callback_data='450_35')
    keyboard135.add(key_250_35, key_350_35, key_450_35)

    if call.data == 'almond':
        txt1 = 'Кофейный напиток с добавлением сиропа миндаль. Украшается маршмэллоу и лепестками миндаля.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1200 тг, 450 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard35)

    if call.data == 'yes35':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard135)

    if call.data == '250_35':
        s =  s + " " + "Миндальный бум" + " " + '250 мл'
        print(s)

    if call.data == '350_35':
        s =  s + " " + "Миндальный бум" + " " + '350 мл'
        print(s)

    if call.data == '450_35':
        s =  s + " " + "Миндальный бум" + " " + '450 мл'
        print(s)

    keyboard36 = types.InlineKeyboardMarkup()
    key_yes36 = types.InlineKeyboardButton(text='Да', callback_data='yes36')
    key_no36 = types.InlineKeyboardButton(text='Нет', callback_data='no36')
    keyboard36.add(key_yes36, key_no36)

    keyboard136 = types.InlineKeyboardMarkup()
    key_250_36 = types.InlineKeyboardButton(text='250 мл', callback_data='250_36')
    key_350_36 = types.InlineKeyboardButton(text='350 мл', callback_data='350_36')
    key_450_36 = types.InlineKeyboardButton(text='450 мл', callback_data='450_36')
    keyboard136.add(key_250_36, key_350_36, key_450_36)

    if call.data == 'raf':
        txt1 = 'Кофейный напиток с добавлением сиропов "Белый шоколад" и "Макадамия".'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1200 тг, 450 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard36)

    if call.data == 'yes36':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard136)

    if call.data == '250_36':
        s =  s + " " + "Рафаэлло" + " " + '250 мл'
        print(s)

    if call.data == '350_36':
        s =  s + " " + "Рафаэлло" + " " + '350 мл'
        print(s)

    if call.data == '450_36':
        s =  s + " " + "Рафаэлло" + " " + '450 мл'
        print(s)

    keyboard37 = types.InlineKeyboardMarkup()
    key_yes37 = types.InlineKeyboardButton(text='Да', callback_data='yes37')
    key_no37 = types.InlineKeyboardButton(text='Нет', callback_data='no37')
    keyboard37.add(key_yes37, key_no37)

    keyboard137 = types.InlineKeyboardMarkup()
    key_250_37 = types.InlineKeyboardButton(text='250 мл', callback_data='250_37')
    key_350_37 = types.InlineKeyboardButton(text='350 мл', callback_data='350_37')
    key_450_37 = types.InlineKeyboardButton(text='450 мл', callback_data='450_37')
    keyboard137.add(key_250_37, key_350_37, key_450_37)

    if call.data == 'salt_latte':
        txt1 = 'Классический латте с добавлением сиропов "Карамельный", "Соленая карамель" и карамельного топинга.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1200 тг, 450 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard37)

    if call.data == 'yes37':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard137)

    if call.data == '250_37':
        s =  s + " " + "Солёный латте XXL" + " " + '250 мл'
        print(s)

    if call.data == '350_37':
        s =  s + " " + "Солёный латте XXL" + " " + '350 мл'
        print(s)

    if call.data == '450_37':
        s =  s + " " + "Солёный латте XXL" + " " + '450 мл'
        print(s)

    keyboard38 = types.InlineKeyboardMarkup()
    key_yes38 = types.InlineKeyboardButton(text='Да', callback_data='yes38')
    key_no38 = types.InlineKeyboardButton(text='Нет', callback_data='no38')
    keyboard38.add(key_yes38, key_no38)

    keyboard138 = types.InlineKeyboardMarkup()
    key_250_38 = types.InlineKeyboardButton(text='250 мл', callback_data='250_38')
    key_350_38 = types.InlineKeyboardButton(text='350 мл', callback_data='350_38')
    key_450_38 = types.InlineKeyboardButton(text='450 мл', callback_data='450_38')
    keyboard138.add(key_250_38, key_350_38, key_450_38)

    if call.data == 'firm':
        txt1 = 'Кофе с добавлением белого шоколада.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 1000 тг, 350 мл - 1200 тг, 450 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard38)

    if call.data == 'yes38':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard138)

    if call.data == '250_38':
        s =  s + " " + "Фирменный кофе RC Coffee" + " " + '250 мл'
        print(s)

    if call.data == '350_38':
        s =  s + " " + "Фирменный кофе RC Coffee" + " " + '350 мл'
        print(s)

    if call.data == '450_38':
        s =  s + " " + "Фирменный кофе RC Coffee" + " " + '450 мл'
        print(s)

    keyboard10 = types.InlineKeyboardMarkup(row_width=1)
    key_matcha = types.InlineKeyboardButton(text='Матча', callback_data='matcha')
    key_matcha_ice = types.InlineKeyboardButton(text='Матча ICE', callback_data='matcha_ice')
    key_kl_apel = types.InlineKeyboardButton(text='Клюква/Апельсин', callback_data='kl_apel')
    key_mango_mar = types.InlineKeyboardButton(text='Манго/Маракуйя', callback_data='mango_mar')
    key_obl_apel = types.InlineKeyboardButton(text='Облепиха/Апельсин', callback_data='obl_apel')
    key_mix = types.InlineKeyboardButton(text='Ягодный микс', callback_data='mix')
    keyboard10.add(key_matcha, key_matcha_ice, key_kl_apel, key_mango_mar, key_obl_apel, key_mix)
    if call.data == 'author_tea':
        bot.send_message(call.message.chat.id, 'Перед тобой список авторского чая', reply_markup=keyboard10, parse_mode='html')

    keyboard39 = types.InlineKeyboardMarkup()
    key_yes39 = types.InlineKeyboardButton(text='Да', callback_data='yes39')
    key_no39 = types.InlineKeyboardButton(text='Нет', callback_data='no39')
    keyboard39.add(key_yes39, key_no39)

    keyboard139 = types.InlineKeyboardMarkup()
    key_250_39 = types.InlineKeyboardButton(text='250 мл', callback_data='250_39')
    key_350_39 = types.InlineKeyboardButton(text='350 мл', callback_data='350_39')
    key_450_39 = types.InlineKeyboardButton(text='450 мл', callback_data='450_39')
    keyboard139.add(key_250_39, key_350_39, key_450_39)

    if call.data == 'matcha':
        txt1 = 'Матча – это японский зеленый чай, растертый в порошок.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='250 мл - 950 тг, 350 мл - 1150 тг, 450 мл - 1250 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard39)

    if call.data == 'yes39':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard139)

    if call.data == '250_39':
        s =  s + " " + "Матча" + " " + '250 мл'
        print(s)

    if call.data == '350_39':
        s =  s + " " + "Матча" + " " + '350 мл'
        print(s)

    if call.data == '450_39':
        s =  s + " " + "Матча" + " " + '450 мл'
        print(s)

    keyboard40 = types.InlineKeyboardMarkup()
    key_yes40 = types.InlineKeyboardButton(text='Да', callback_data='yes40')
    key_no40 = types.InlineKeyboardButton(text='Нет', callback_data='no40')
    keyboard40.add(key_yes40, key_no40)

    keyboard140 = types.InlineKeyboardMarkup()
    key_250_40 = types.InlineKeyboardButton(text='250 мл', callback_data='250_40')
    key_350_40 = types.InlineKeyboardButton(text='350 мл', callback_data='350_40')
    key_450_40 = types.InlineKeyboardButton(text='450 мл', callback_data='450_40')
    keyboard140.add(key_250_40, key_350_40, key_450_40)

    if call.data == 'matcha_ice':
        txt1 = 'Матча – это японский зеленый чай, растертый в порошок охлажденный.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='300 мл - 1150 тг, 400 мл - 1250 тг, 500 мл - 1400 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard40)

    if call.data == 'yes40':
        txt = 'Объем?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard140)

    if call.data == '250_40':
        s =  s + " " + "Матча ICE" + " " + '250 мл'
        print(s)

    if call.data == '350_40':
        s =  s + " " + "Матча ICE" + " " + '350 мл'
        print(s)

    if call.data == '450_40':
        s =  s + " " + "Матча ICE" + " " + '450 мл'
        print(s)

    keyboard41 = types.InlineKeyboardMarkup()
    key_yes41 = types.InlineKeyboardButton(text='Да', callback_data='yes41')
    key_no41 = types.InlineKeyboardButton(text='Нет', callback_data='no41')
    keyboard41.add(key_yes41, key_no41)

    keyboard141 = types.InlineKeyboardMarkup(row_width=1)
    key_klyukva = types.InlineKeyboardButton(text='Клюква', callback_data='klyukva')
    key_apelsin = types.InlineKeyboardButton(text='Апельсин', callback_data='apelsin')
    keyboard141.add(key_klyukva, key_apelsin)

    if call.data == 'kl_apel':
        txt1 = 'Клюквенный чай с апельсином и медом.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 750 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard41)

    if call.data == 'yes41':
        txt = 'Клюква или апельсин?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard141)

    if call.data == 'klyukva':
        s =  s + " " + "Клюква" + " " + '350 мл'
        print(s)

    if call.data == 'apelsin':
        s =  s + " " + "Апельсин" + " " + '350 мл'
        print(s)

    keyboard42 = types.InlineKeyboardMarkup()
    key_yes42 = types.InlineKeyboardButton(text='Да', callback_data='yes42')
    key_no42 = types.InlineKeyboardButton(text='Нет', callback_data='no42')
    keyboard42.add(key_yes42, key_no42)

    keyboard142 = types.InlineKeyboardMarkup(row_width=1)
    key_mango = types.InlineKeyboardButton(text='Маго', callback_data='mango')
    key_marakuya = types.InlineKeyboardButton(text='Маракуйя', callback_data='marakuya')
    keyboard142.add(key_mango, key_marakuya)

    if call.data == 'mango_mar':
        txt1 = 'Зеленый чай с манго и пюре маракуйя.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 750 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard42)

    if call.data == 'yes42':
        txt = 'Манго или маракуйя?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard142)

    if call.data == 'mango':
        s =  s + " " + "Манго" + " " + '350 мл'
        print(s)

    if call.data == 'marakuya':
        s =  s + " " + "Маракуйя" + " " + '350 мл'
        print(s)

    keyboard43 = types.InlineKeyboardMarkup()
    key_yes43 = types.InlineKeyboardButton(text='Да', callback_data='yes43')
    key_no43 = types.InlineKeyboardButton(text='Нет', callback_data='no43')
    keyboard43.add(key_yes43, key_no43)

    keyboard143 = types.InlineKeyboardMarkup(row_width=1)
    key_oblep = types.InlineKeyboardButton(text='Облепиха', callback_data='oblep')
    key_apel_2 = types.InlineKeyboardButton(text='Апельсин', callback_data='apel_2')
    keyboard143.add(key_oblep, key_apel_2)

    if call.data == 'obl_apel':
        txt1 = 'Облепиховый чай с апельсином, мёдом и палочкой корицы.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 750 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard43)

    if call.data == 'yes43':
        txt = 'Облепиха или апельсин?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard143)

    if call.data == 'oblep':
        s =  s + " " + "Облепиха" + " " + '350 мл'
        print(s)

    if call.data == 'apel_2':
        s =  s + " " + "Апельсин" + " " + '350 мл'
        print(s)

    keyboard44 = types.InlineKeyboardMarkup()
    key_yes44 = types.InlineKeyboardButton(text='Да', callback_data='yes44')
    key_no44 = types.InlineKeyboardButton(text='Нет', callback_data='no44')
    keyboard44.add(key_yes44, key_no44)

    if call.data == 'mix':
        txt1 = 'Чай английский завтрак с ягодами клубники, смородины, ежевики, а так же лимоном.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 750 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard44)

    if call.data == 'yes44':
        s =  s + " " + "Ягодный микс" + " " + '350 мл'
        print(s)

    keyboard11 = types.InlineKeyboardMarkup(row_width=1)
    key_english_breakfast = types.InlineKeyboardButton(text='Английский завтрак', callback_data='english_breakfast')
    key_jasmin = types.InlineKeyboardButton(text='Жасминовый чай', callback_data='jasmin')
    key_green = types.InlineKeyboardButton(text='Зеленый чай', callback_data='green')
    key_imbir = types.InlineKeyboardButton(text='Имбирный чай', callback_data='imbir')
    key_erl_gray = types.InlineKeyboardButton(text='Эрл грэй', callback_data='erl_gray')
    keyboard11.add(key_english_breakfast, key_jasmin, key_green, key_imbir, key_erl_gray)
    if call.data == 'classic_tea':
        bot.send_message(call.message.chat.id, 'Перед тобой список классического чая', reply_markup=keyboard11, parse_mode='html')

    keyboard45 = types.InlineKeyboardMarkup()
    key_yes45 = types.InlineKeyboardButton(text='Да', callback_data='yes45')
    key_no45 = types.InlineKeyboardButton(text='Нет', callback_data='no45')
    keyboard45.add(key_yes45, key_no45)

    if call.data == 'english_breakfast':
        txt1 = 'Насыщенный крепкий черный чай.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 550 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard45)

    if call.data == 'yes45':
        s =  s + " " + "Английский завтрак" + " " + '350 мл'
        print(s)

    keyboard46 = types.InlineKeyboardMarkup()
    key_yes46 = types.InlineKeyboardButton(text='Да', callback_data='yes46')
    key_no46 = types.InlineKeyboardButton(text='Нет', callback_data='no46')
    keyboard46.add(key_yes46, key_no46)

    if call.data == 'jasmin':
        txt1 = 'Чай с добавлением цветков жасмина, имеет утонченный сладкий аромат.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 550 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard46)

    if call.data == 'yes46':
        s =  s + " " + "Жасминовый чай" + " " + '350 мл'
        print(s)

    keyboard47 = types.InlineKeyboardMarkup()
    key_yes47 = types.InlineKeyboardButton(text='Да', callback_data='yes47')
    key_no47 = types.InlineKeyboardButton(text='Нет', callback_data='no47')
    keyboard47.add(key_yes47, key_no47)

    if call.data == 'green':
        txt1 = 'Чай английский завтрак с ягодами клубники, смородины, ежевики, а так же лимоном.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 550 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard47)

    if call.data == 'yes47':
        s =  s + " " + "Зеленый чай" + " " + '350 мл'
        print(s)

    keyboard48 = types.InlineKeyboardMarkup()
    key_yes48 = types.InlineKeyboardButton(text='Да', callback_data='yes48')
    key_no48 = types.InlineKeyboardButton(text='Нет', callback_data='no48')
    keyboard48.add(key_yes48, key_no48)

    if call.data == 'imbir':
        txt1 = 'Чай с добавлением имбиря.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 550 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard48)

    if call.data == 'yes48':
        s =  s + " " + "Имбирный чай" + " " + '350 мл'
        print(s)

    keyboard49 = types.InlineKeyboardMarkup()
    key_yes49 = types.InlineKeyboardButton(text='Да', callback_data='yes49')
    key_no49 = types.InlineKeyboardButton(text='Нет', callback_data='no49')
    keyboard49.add(key_yes49, key_no49)

    if call.data == 'erl_gray':
        txt1 = 'Чёрный чай с добавлением масла, полученного из кожуры плодов бергамота.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='350 мл - 550 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard49)

    if call.data == 'yes49':
        s =  s + " " + "Эрл грэй" + " " + '350 мл'
        print(s)

    keyboard12 = types.InlineKeyboardMarkup(row_width=1)
    key_donuts = types.InlineKeyboardButton(text='Донаты', callback_data='donuts')
    key_desert_1 = types.InlineKeyboardButton(text='Десерт', callback_data='desert_1')
    key_bake = types.InlineKeyboardButton(text='Выпечка', callback_data='bake')
    keyboard12.add(key_donuts, key_desert_1, key_bake)
    if call.data == 'desert':
        bot.send_message(call.message.chat.id, text='Давай выберем десерт:', reply_markup=keyboard12)

    keyboard13 = types.InlineKeyboardMarkup(row_width=1)
    key_kokos = types.InlineKeyboardButton(text='Донат "Кокосовый"', callback_data='kokos')
    key_les = types.InlineKeyboardButton(text='Донат "Лесные ягоды"', callback_data='les')
    key_3_choc = types.InlineKeyboardButton(text='Донат "Тройной шоколад"', callback_data='3_choc')
    key_choc_wh = types.InlineKeyboardButton(text='Донат "Шоколадный с белой глазурью"', callback_data='choc_wh')
    key_karam = types.InlineKeyboardButton(text='Донат "Карамельный"', callback_data='karam')
    key_strawberry = types.InlineKeyboardButton(text='Донат "Клубничный"', callback_data='strawberry')
    key_apple_kor = types.InlineKeyboardButton(text='Донат "Яблоко-корица"', callback_data='apple_kor')
    key_lemon = types.InlineKeyboardButton(text='Донат "Лимонный"', callback_data='lemon')
    key_salt_karam = types.InlineKeyboardButton(text='Донат "Соленая карамель"', callback_data='salt_karam')
    keyboard13.add(key_kokos, key_les, key_3_choc, key_choc_wh, key_karam, key_strawberry, key_apple_kor, key_lemon, key_salt_karam)
    if call.data == 'donuts':
        bot.send_message(call.message.chat.id, 'Перед тобой список донатов:', reply_markup=keyboard13, parse_mode='html')

    keyboard50 = types.InlineKeyboardMarkup()
    key_yes50 = types.InlineKeyboardButton(text='Да', callback_data='yes50')
    key_no50 = types.InlineKeyboardButton(text='Нет', callback_data='no50')
    keyboard50.add(key_yes50, key_no50)

    if call.data == 'kokos':
        txt1 = 'Донат с кокосовой начинкой, украшенный кокосовой стружкой.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard50)

    if call.data == 'yes50':
        s =  s + " " + 'Донат "Кокосовый"'
        print(s)

    keyboard51 = types.InlineKeyboardMarkup()
    key_yes51 = types.InlineKeyboardButton(text='Да', callback_data='yes51')
    key_no51 = types.InlineKeyboardButton(text='Нет', callback_data='no51')
    keyboard51.add(key_yes51, key_no51)

    if call.data == 'les':
        txt1 = 'Донат с начинкой "лесные ягоды" и розовой глазурью с розовой посыпкой.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard51)

    if call.data == 'yes51':
        s =  s + " " + 'Донат "Лесные ягоды"'
        print(s)

    keyboard52 = types.InlineKeyboardMarkup()
    key_yes52 = types.InlineKeyboardButton(text='Да', callback_data='yes52')
    key_no52 = types.InlineKeyboardButton(text='Нет', callback_data='no52')
    keyboard52.add(key_yes52, key_no52)

    if call.data == '3_choc':
        txt1 = 'Донат с шоколадной начинкой, шоколадной глазурью и шоколадной посыпкой.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard52)

    if call.data == 'yes52':
        s =  s + " " + 'Донат "Тройной шоколад"'
        print(s)

    keyboard53 = types.InlineKeyboardMarkup()
    key_yes53 = types.InlineKeyboardButton(text='Да', callback_data='yes53')
    key_no53 = types.InlineKeyboardButton(text='Нет', callback_data='no53')
    keyboard53.add(key_yes53, key_no53)

    if call.data == 'choc_wh':
        txt1 = 'Донат с начинкой из шоколадного крема, украшенный белой глазурью и посыпкой из какао.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard53)

    if call.data == 'yes53':
        s =  s + " " + 'Донат "Шоколадный с белой глазурью"'
        print(s)

    keyboard54 = types.InlineKeyboardMarkup()
    key_yes54 = types.InlineKeyboardButton(text='Да', callback_data='yes54')
    key_no54 = types.InlineKeyboardButton(text='Нет', callback_data='no54')
    keyboard54.add(key_yes54, key_no54)

    if call.data == 'karam':
        txt1 = 'Донат глазированный со вкусом какао со сладкой карамельной начинкой.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard54)

    if call.data == 'yes54':
        s =  s + " " + 'Донат "Карамельный"'
        print(s)

    keyboard55 = types.InlineKeyboardMarkup()
    key_yes55 = types.InlineKeyboardButton(text='Да', callback_data='yes55')
    key_no55 = types.InlineKeyboardButton(text='Нет', callback_data='no55')
    keyboard55.add(key_yes55, key_no55)

    if call.data == 'strawberry':
        txt1 = 'Донат с глазурью со вкусом клубники, с клубничной начинкой внутри.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard55)

    if call.data == 'yes55':
        s =  s + " " + 'Донат "Клубничный"'
        print(s)

    keyboard56 = types.InlineKeyboardMarkup()
    key_yes56 = types.InlineKeyboardButton(text='Да', callback_data='yes56')
    key_no56 = types.InlineKeyboardButton(text='Нет', callback_data='no56')
    keyboard56.add(key_yes56, key_no56)

    if call.data == 'apple_kor':
        txt1 = 'Донат с двойной начинкой из корицы и яблок, декорированный сахаром.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard56)

    if call.data == 'yes56':
        s =  s + " " + 'Донат "Яблоко-корица"'
        print(s)

    keyboard57 = types.InlineKeyboardMarkup()
    key_yes57 = types.InlineKeyboardButton(text='Да', callback_data='yes57')
    key_no57 = types.InlineKeyboardButton(text='Нет', callback_data='no57')
    keyboard57.add(key_yes57, key_no57)

    if call.data == 'lemon':
        txt1 = 'Донат с лимонной начинкой, украшенный белой глазурью и жёлтой посыпкой.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard57)

    if call.data == 'yes57':
        s =  s + " " + 'Донат "Лимонный"'
        print(s)

    keyboard58 = types.InlineKeyboardMarkup()
    key_yes58 = types.InlineKeyboardButton(text='Да', callback_data='yes58')
    key_no58 = types.InlineKeyboardButton(text='Нет', callback_data='no58')
    keyboard58.add(key_yes58, key_no58)

    if call.data == 'salt_karam':
        txt1 = 'Донат с солёной карамелью, украшенный белым топпингом и толчеными орехами.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='700 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard58)

    if call.data == 'yes58':
        s =  s + " " + 'Донат "Соленая карамель"'
        print(s)

    keyboard14 = types.InlineKeyboardMarkup(row_width=1)
    key_mango_mar_pir = types.InlineKeyboardButton(text='Пирожное "Манго-магакуйя"', callback_data='mango_mar_pir')
    key_tiramisu = types.InlineKeyboardButton(text='Пирожное "Тирамису Маскарпоне"', callback_data='tiramisu')
    key_choc_bom = types.InlineKeyboardButton(text='Пирожное "Шоколадная бомба"', callback_data='choc_bom')
    keyboard14.add(key_mango_mar_pir, key_tiramisu, key_choc_bom)
    if call.data == 'desert_1':
        bot.send_message(call.message.chat.id, 'Перед тобой список десертов:', reply_markup=keyboard14, parse_mode='html')

    keyboard59 = types.InlineKeyboardMarkup()
    key_yes59 = types.InlineKeyboardButton(text='Да', callback_data='yes59')
    key_no59 = types.InlineKeyboardButton(text='Нет', callback_data='no59')
    keyboard59.add(key_yes59, key_no59)

    if call.data == 'mango_mar_pir':
        txt1 = 'Нежнейшее суфле из манго с сердцевиной из кокосового суфле из свежих сливок с ароматной начинкой из мякоти маракуйи с кислинкой на корже из кокосовой стружки.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='2200 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard59)

    if call.data == 'yes59':
        s =  s + " " + 'Пирожное "Манго-магакуйя"'
        print(s)

    keyboard60 = types.InlineKeyboardMarkup()
    key_yes60 = types.InlineKeyboardButton(text='Да', callback_data='yes60')
    key_no60 = types.InlineKeyboardButton(text='Нет', callback_data='no60')
    keyboard60.add(key_yes60, key_no60)

    if call.data == 'tiramisu':
        txt1 = 'Два слоя крем-сыра маскарпоне на печенье Савоярди, пропитанном кофе. Украшено сверху какао.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='2300 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard60)

    if call.data == 'yes60':
        s =  s + " " + 'Пирожное "Тирамису Маскарпоне"'
        print(s)

    keyboard61 = types.InlineKeyboardMarkup()
    key_yes61 = types.InlineKeyboardButton(text='Да', callback_data='yes61')
    key_no61 = types.InlineKeyboardButton(text='Нет', callback_data='no61')
    keyboard61.add(key_yes61, key_no61)

    if call.data == 'choc_bom':
        txt1 = 'Два слоя из белого и темного шоколада с хрустящей сердцевиной из фундучного пралине, покрыто молочным шоколадом.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='2300 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard61)
    
    if call.data == 'yes61':
        s =  s + " " + 'Пирожное "Шоколадная бомба"'
        print(s)

    keyboard15 = types.InlineKeyboardMarkup()
    key_tart = types.InlineKeyboardButton(text='Тарталетка Малиновая', callback_data='tart')
    keyboard15.add(key_tart)
    if call.data == 'bake':
        bot.send_message(call.message.chat.id, 'Перед тобой список нашей выпечки:', reply_markup=keyboard15, parse_mode='html')

    keyboard62 = types.InlineKeyboardMarkup()
    key_yes62 = types.InlineKeyboardButton(text='Да', callback_data='yes62')
    key_no62 = types.InlineKeyboardButton(text='Нет', callback_data='no62')
    keyboard62.add(key_yes62, key_no62)

    if call.data == 'tart':
        txt1 = 'Заварной крем, взбитые сливки и спелая малина в корзиночке из песочного теста.'
        bot.send_message(call.message.chat.id, text=txt1)
        # img = open('americano_ice.avif', 'rb')
        # bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text='1800 тг')
        txt = 'Добавить к заказу?'
        bot.send_message(call.message.chat.id, txt, reply_markup=keyboard62)

    if call.data == 'yes62':
        s =  s + " " + 'Тарталетка Малиновая'
        print(s)

    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id) 
    # Чтобы кнопки удалялись

# bot.polling(none_stop=True)

bot.polling(none_stop=True)