from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import actbutton
from sheets_function import sheets_functions


# @dp.message_handler(commands=['start'])
async def cm_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добрый день', reply_markup=actbutton)


# @dp.message_handler(commands=['Найти дежурного'])
async def worker_finder(message: types.Message):
    await message.reply(f'{sheets_functions.get_worker()}', reply_markup=actbutton)


@dp.callback_query_handler(text='find_button')
async def worker_finder_query(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f'{sheets_functions.get_worker()}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['start'])
    dp.register_message_handler(worker_finder, commands=['Найти дежурного'])

