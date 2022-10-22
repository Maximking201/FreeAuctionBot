import telebot
from telebot import types
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from random import randint

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1032504138866630746/mu11CNhkXupJlvOTSwxKdkJPOVnluK3KfZFxR0n7hIZz7GOvheUgpztsYWs0oUCM_Gh-')
bot = telebot.TeleBot("5656642096:AAF5EKeoDmaK3F62VjyCO2piY7OHT8BNhSk")
whitelist = []
invitelink = "https://discord.gg/U7q4efmeab"
now = datetime.now()

class Account:
    def __init__(self, name, password, recovery, pin, id_acc):
        self.username = name
        self.password = password
        self.recovery = recovery
        self.pin = pin
        self.id = id_acc

WASTER_YT1 = Account("WASTER_YT1", "asdahuysdadp123_!", ["fhg5kxpu9","sdt71bjzk","p3to7sc57","baalzi0gq","zl3ypmlvh","461fpn4ow","j1ky2p2ot","8hnk8uuuo","s1mgdkkj9","f7vxrlvzq"], "1892", "3292602177")
fitfyt_21 = Account("Ilovehotbebra2228", "asyd8hsadyoahydasd!2123234asudhad0a9uh", ["47jyudjp5","aytmegs4r","zhv94zno4","sgbhjhlau","ou6l9bzqt","etef2rq3y","s5cukfk2i","33ombevdj","voitjmfj6","zmpu2rs4f"], "6742", "2979972964")

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.username not in whitelist:
        gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
        gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
        if randint(1,2) == 1:
            bot.send_message(message.chat.id, f'ээээ иди нахуй')
            bot.send_animation(message.chat.id,f'{gif1}')
        elif randint(1,3) == 2:
            bot.send_message(message.chat.id, f'ээээ иди нахуй')
            bot.send_animation(message.chat.id,f'{gif2}')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🥱 Что делает это бот?")
        button2 = types.KeyboardButton("🤖 Получить аккаунты")
        button3 = types.KeyboardButton("👀 Получить ссылку на дискорд")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, f'👋🏿 Привет, {message.from_user.first_name}', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🥱 Что делает это бот?"):
        if message.from_user.username not in whitelist:
            gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
            gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
            if randint(1,2) == 1:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif1}')
            elif randint(1,3) == 2:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif2}')
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👎🏿 Вернуться назад")
            markup.add(button1)
            bot.send_message(message.chat.id, text="Этот бот был создан для админов сервер Are Robux Games Scam, чтобы хранить данные от аккаунтов", reply_markup=markup)
    elif(message.text == "🤖 Получить аккаунты"):
        if message.from_user.username not in whitelist:
            gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
            gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
            if randint(1,2) == 1:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif1}')
            elif randint(1,3) == 2:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif2}')
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👎🏿 Вернуться назад")
            button_account1 = types.KeyboardButton("WASTER_YT1")
            button_account2 = types.KeyboardButton("fitfyt_21")
            markup.add(button1, button_account1, button_account2)
            bot.send_message(message.chat.id, text="🤖 Выберите аккаунты", reply_markup=markup)
    elif(message.text == "👀 Получить ссылку на дискорд"):
        if message.from_user.username not in whitelist:
            gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
            gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
            if randint(1,2) == 1:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif1}')
            elif randint(1,3) == 2:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif2}')
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👎🏿 Вернуться назад")
            markup.add(button1)
            bot.send_message(message.chat.id, text=f"{invitelink}", reply_markup=markup)
    elif(message.text == "WASTER_YT1"):
        if message.from_user.username not in whitelist:
            gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
            gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
            if randint(1,2) == 1:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif1}')
            elif randint(1,3) == 2:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif2}')
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👎🏿 Вернуться назад")
            markup.add(button1)
            bot.send_message(message.chat.id, f'Ник: {WASTER_YT1.username} Пароль: {WASTER_YT1.password} Пин-код: {WASTER_YT1.pin}' , reply_markup=markup)
    elif(message.text == "fitfyt_21"):
        if message.from_user.username not in whitelist:
            gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
            gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
            if randint(1,2) == 1:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif1}')
            elif randint(1,3) == 2:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif2}')
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👎🏿 Вернуться назад")
            markup.add(button1)
            bot.send_message(message.chat.id, f'Ник: {fitfyt_21.username} Пароль: {fitfyt_21.password} Пин-код: {fitfyt_21.pin}', reply_markup=markup)
    elif(message.text == "👎🏿 Вернуться назад"):
        if message.from_user.username not in whitelist:
            gif1 = 'https://tenor.com/view/raiden-raiden-metal-gear-metal-gear-rising-metal-gear-armstrong-metal-gear-gif-25495293'
            gif2 = 'https://tenor.com/view/cares-metal-gear-rising-metal-gear-rising-cares-jetstream-sam-jetstream-sam-cares-gif-25395907'
            if randint(1,2) == 1:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif1}')
            elif randint(1,3) == 2:
                bot.send_message(message.chat.id, f'ээээ иди нахуй')
                bot.send_animation(message.chat.id,f'{gif2}')
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("🥱 Что делает это бот?")
            button2 = types.KeyboardButton("🤖 Получить аккаунты")
            button3 = types.KeyboardButton("👀 Получить ссылку на дискорд")
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, f'👋🏿 Снова привет, {message.from_user.first_name}', reply_markup=markup)
    
    


bot.polling(none_stop=True)