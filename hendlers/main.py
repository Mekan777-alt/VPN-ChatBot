from aiogram import types
from config import dp
from aiogram.types import ReplyKeyboardMarkup


@dp.message_handler(commands='start')
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('VPN - 1 месяц')
    markup.add('VPN - 3 месяца -10% скидка')
    markup.add('VPN - 6 месяцев -15% скидка')
    markup.add('VPN - 12 месяцев -20% скидка')
    await message.answer('Здравствуйте!', reply_markup=markup)


@dp.message_handler(text='VPN - 1 месяц')
async def one_month(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Оплатить")
    await message.answer("Стоимость за 1 месяц состовляет 180 рублей", reply_markup=markup)


@dp.message_handler(text='VPN - 3 месяца -10% скидка')
async def three_month(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Оплатить")
    price = (180 * 3) - (180 * 3 / 100 * 10)
    await message.answer(f"Стоимость за 3 месяцa состовляет {price} рублей", reply_markup=markup)


@dp.message_handler(text='VPN - 6 месяцев -15% скидка')
async def six_month(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Оплатить")
    price = (180 * 6) - (180 * 6 / 100 * 15)
    await message.answer(f"Стоимость за 6 месяцев состовляет {price} рублей", reply_markup=markup)


@dp.message_handler(text='VPN - 12 месяцев -20% скидка')
async def twenty_month(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Оплатить")
    price = (180 * 12) - (180 * 12 / 100 * 20)
    await message.answer(f"Стоимость за 12 месяцев состовляет {price} рублей", reply_markup=markup)
