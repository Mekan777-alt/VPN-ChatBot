from aiogram import Dispatcher, Bot, types
from local_config import token
from data.data import Database
import os

token = token
path = os.getcwd() + '/data/database.db'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
db = Database(path)
