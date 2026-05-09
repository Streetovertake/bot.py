# bot.py
import telebot

TOKEN = "8745099851:AAECZh-bIjKQQNhTpOl3sUAxQ-SMKzO9Bxk"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):

    bot.send_message(message.chat.id, "Бот работает 🚀")

bot.infinity_polling()