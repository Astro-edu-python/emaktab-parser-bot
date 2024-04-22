import logging

from aiogram import executor, Bot, Dispatcher

from config import BOT_TOKEN
from emaktab_bot.handlers.commands import register_commands_handlers
from emaktab_bot.handlers.emaktab import register_emaktab_handlers

logging.basicConfig(level='INFO')


bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


if __name__ == '__main__':
    register_commands_handlers(dp)
    register_emaktab_handlers(dp)
    executor.start_polling(dp)
