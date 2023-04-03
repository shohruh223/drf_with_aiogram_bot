from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def get_product():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("/product")
    rkm.add(btn)
    return rkm


def get_inline_product():
    ikm = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("all product", callback_data="all product")
    btn2 = InlineKeyboardButton("add product", callback_data="add product")
    ikm.add(btn, btn2)
    return ikm