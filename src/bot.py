import os

import telebot

bot = telebot.TeleBot(os.environ["anonymous_bot_token"], parse_mode="HTML")
