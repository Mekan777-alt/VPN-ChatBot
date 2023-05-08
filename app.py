import logging
from config import dp
from aiogram import executor


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)