from aiogram import Dispatcher, Bot
from aiogram.types import Message, BotCommand

from emaktab_bot.constants.commands import UserCommands
from emaktab_bot.handlers.emaktab import (
    start_class_parse_info, parse_week_lessons_command
)
from emaktab_bot.keyboards.reply import START_COMMANDS_KEYBOARD


async def init_user_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command, value.value)
            for command, value in UserCommands.__members__.items()
        ]
    )


async def start(message: Message):
    await init_user_commands(message.bot)
    await message.answer(
        'Приветствую👋\nЯ бот-парсер emaktab!\nВыберите команду',
        reply_markup=START_COMMANDS_KEYBOARD
    )


def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=[UserCommands.start.name])
    dp.register_message_handler(
        start_class_parse_info,
        commands=[UserCommands.parseinfo.name]
    )
    dp.register_message_handler(
        parse_week_lessons_command,
        commands=[UserCommands.parseschedule.name]
    )
