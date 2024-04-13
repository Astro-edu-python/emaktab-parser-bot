from aiogram import Dispatcher
from aiogram.types import Message


async def echo(message: Message):
    await message.answer(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
