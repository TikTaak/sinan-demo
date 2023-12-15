# import telebot
import os
from dotenv import load_dotenv

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Admin(object):
    admins = [1069660169]
    def send_message(self, message):
        for admin in self.admins:
            bot.send_message(admin, message)
            return None
admins = Admin()
        
        
    
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


