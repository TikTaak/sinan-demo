# import telebot
import os
from dotenv import load_dotenv

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


bot.infinity_polling()
