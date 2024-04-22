from aiogram import Dispatcher
from aiogram.types import Message
from celery.result import AsyncResult

from config import EMAKTAB_LOGIN, EMAKTAB_PASSWORD
from emaktab_bot.constants.commands import UserReplyBtnCommands
from emaktab_bot.services.emaktab_tasks.tasks import parse_week_lessons


async def start_class_parse_info(message: Message):
    await message.reply('Запускаю задачу...⏳')
    task: AsyncResult = parse_week_lessons.delay(
        message.bot._token, EMAKTAB_LOGIN, EMAKTAB_PASSWORD,
        message.from_user.id
    )
    await message.reply(
        'Запустил задачу по парсингу информаций о классе\n'
        f'<b>ID задачи: {task.task_id}</b>'
    )


async def parse_week_lessons_command(message: Message):
    await message.reply('Запускаю задачу...⏳')
    task: AsyncResult = parse_week_lessons.delay(
        message.bot._token, EMAKTAB_LOGIN, EMAKTAB_PASSWORD,
        message.from_user.id
    )
    await message.reply(
        f'Запустил задачу по парсингу расписаний.\n'
        f'<b>ID задачи: {task.task_id}</b>'
    )


def register_emaktab_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_class_parse_info,
        text=UserReplyBtnCommands.class_info_parse.value
    )
    dp.register_message_handler(
        parse_week_lessons_command,
        text=UserReplyBtnCommands.class_schedule_parse.value
    )
