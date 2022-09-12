from email import message
import os

import emoji
from loguru import logger
from telebot import types

from src.constant import keyboards
from src.filters import IsAdmin
from src.utils.io import write_json
from src.bot import bot


class Bot:
    """
    Telegram bot to randomly connect to strangers to talk
    """

    def __init__(self, telebot) -> None:
        self.bot = telebot

        self.bot.add_custom_filter(IsAdmin())

        self.handlers()

    def handlers(self):
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(
                message.chat.id, f"<strong>You are admin of group</strong>"
            )

        @self.bot.message_handler(func=lambda _: True)
        def echo_all(message):
            self.send_message(
                message.chat.id, message.text, reply_markup=keyboards.main
            )

    def run(self):
        logger.info("bot started")
        self.bot.infinity_polling()

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        if emojize:
            text = emoji.emojize(text)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)


if __name__ == "__main__":
    bot = Bot(telebot=bot)
    bot.run()
