from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TOKEN_API
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)
