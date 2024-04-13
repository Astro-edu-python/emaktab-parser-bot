import logging

from aiogram import executor, Bot, Dispatcher

from config import BOT_TOKEN
from emaktab_bot.handlers.echo import register_handlers

logging.basicConfig(level='INFO')


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp)
