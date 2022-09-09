import emoji
from telebot import types


def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    """create keyboard from list of keys

    Args:
        row_width (int, optional): max number of keys in a row. Defaults to 2.
        resize_keyboard (bool, optional): Defaults to True.
    """
    markup = types.ReplyKeyboardMarkup(
        row_width=row_width, resize_keyboard=resize_keyboard
    )
    keys = map(emoji.emojize, keys)
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)

    return markup
