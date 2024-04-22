from aiogram.types import ReplyKeyboardMarkup

import emaktab_bot.buttons.commands as e_com_btns

START_COMMANDS_KEYBOARD = ReplyKeyboardMarkup([
    [
        e_com_btns.PARSE_CLASS_INFO_BTN, e_com_btns.PARSE_SCHEDULE_BTN
    ],
], resize_keyboard=True)
