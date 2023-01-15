import telebot
import sqlite3
from telebot import types
import config
import random
import secrets


API_TOKEN = secrets.a

bot = telebot.TeleBot(API_TOKEN)
con = sqlite3.connect('gadalka.db', check_same_thread=False)
cursor = con.cursor()
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dob = types.KeyboardButton("Добавить фразу")
    pok = types.KeyboardButton("Посмотреть записанные фразы")
    bla = types.KeyboardButton("Удалить фразу")
    ran = types.KeyboardButton("Выдать рандомную фразу")
    delt = types.KeyboardButton("Очистить список слов")
    markup.add(dob,pok,bla,ran,delt)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я гадалка хагги ваги, что бы узнать что я умею зайди в меню".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if (message.text == "Добавить фразу"):
        i = message.chat.id
        j = bot.send_message(i, 'Напишите фразу которую хотите добавить:')
        bot.register_next_step_handler(j , sel)
    if (message.text == "Посмотреть записанные фразы"):
        l = message.chat.id
        saved = cursor.execute("SELECT * FROM frazes")
        bot.send_message(l, f'{saved.fetchall()}')
    if (message.text == "Удалить фразу"):
        y = message.chat.id
        u = bot.send_message(y, f'Введите номер фразы(отсчет ведется от 0):')
        bot.register_next_step_handler(u, delik)
    if (message.text == "Очистить список слов"):
        ll(o = 'tunch')
        bot.send_message( message.chat.id, f'Cписок очищен')
    if (message.text == "Выдать рандомную фразу"):
        qu = message.chat.id
        saved = cursor.execute("SELECT * FROM frazes")
        po = bot.send_message(qu, 'Рандомная фраза:')
        bot.send_message(message.chat.id, f'{random.choice(list(saved.fetchall()))}')
def hw(added: str):
    cursor.execute("INSERT INTO frazes VALUES(?);", (f"{added}",))
    con.commit()
def ll(o: str):
    cursor.execute(f"DELETE FROM frazes;")
    con.commit()
def pere(o: str):
    cursor.execute("INSERT INTO frazes VALUES(?);", (f"{o}",))
    con.commit()
def sel(message):
    i = message.chat.id
    t = message.text
    hw(added = t)
    saved = cursor.execute("SELECT * FROM frazes")
    bot.send_message(i, f'Фраза добавлена')
def delik(message):
    p = message.text
    saved = cursor.execute("SELECT * FROM frazes")
    w = int(p)
    f = list(saved.fetchall())
    del f[w]
    ll(o = p)
    #qw = tuple(f)
    for i in f:
        pere(o = i)
    bot.send_message(message.chat.id, f'Фраза удалена')
#: {saved.fetchall()}  если понадобится выводить список


bot.infinity_polling()
