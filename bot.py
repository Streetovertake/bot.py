import telebot import os

TOKEN = os.getenv("TOKEN")

if not TOKEN: raise Exception("TOKEN не найден в переменных окружения")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) def start(message): bot.send_message( message.chat.id, "Привет 👋\nБот работает 24/7 🚀" )

@bot.message_handler(commands=['help']) def help_cmd(message): bot.send_message( message.chat.id, "Команды:\n/start - запуск\n/help - помощь" )

bot.infinity_polling()