# import telebot
import os
from dotenv import load_dotenv

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
class Admin(object):
    admins = config.ADMINS_TELEGRAM_ID
    def send_message(self, message):
        for admin in self.admins:
            bot.send_message(admin, message)
            return None
admins = Admin()
        
        
    
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


