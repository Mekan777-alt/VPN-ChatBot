from config import dp
from aiogram import types


@dp.message_handler(commands='admin')
async def admin(message: types.Message):
    pass
