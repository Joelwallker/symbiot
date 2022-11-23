from aiogram.utils import executor
from create_bot import dp
from handlers import client

client.register_handlers_client(dp)


async def on_startup(_):
    print('Online')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



