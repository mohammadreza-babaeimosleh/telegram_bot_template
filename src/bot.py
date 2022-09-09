import os

import emoji
import telebot
from loguru import logger
from telebot import types

from src.constant import keyboards
from src.utils.io import write_json


class Bot:
    """
    Telegram bot to randomly connect to strangers to talk
    """

    def __init__(self) -> None:
        self.bot = telebot.TeleBot(os.environ["anonymous_bot_token"])
        self.echo_all = self.bot.message_handler(func=lambda m: True)(self.echo_all)

    def run(self):
        logger.info("bot started")
        self.bot.infinity_polling()

    def echo_all(self, message):
        write_json(message.json, "message.json")
        self.bot.send_message(
            message.chat.id, message.text, reply_markup=keyboards.main
        )


if __name__ == "__main__":
    bot = Bot()
    bot.run()
