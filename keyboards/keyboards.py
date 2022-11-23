from aiogram.types import ReplyKeyboardMarkup,  \
    InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove


actbutton1 = InlineKeyboardButton(text='Найти дежурного', callback_data='find_button')
actbutton2 = InlineKeyboardButton(text='Пнуть дежурного', callback_data='sand_button')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
actbutton = InlineKeyboardMarkup(row_width=1)


actbutton.add(actbutton1)

