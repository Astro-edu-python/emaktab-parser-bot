from aiogram.types import KeyboardButton

from emaktab_bot.constants.commands import UserReplyBtnCommands

PARSE_CLASS_INFO_BTN = KeyboardButton(
    UserReplyBtnCommands.class_info_parse.value
)
PARSE_SCHEDULE_BTN = KeyboardButton(
    UserReplyBtnCommands.class_schedule_parse.value
)
