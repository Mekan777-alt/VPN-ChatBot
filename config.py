from aiogram import Dispatcher, Bot
from local_config import token

token = token

bot = Bot(token=token)
dp = Dispatcher(bot)
