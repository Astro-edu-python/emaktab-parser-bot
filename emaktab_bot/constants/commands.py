from enum import Enum


class UserReplyBtnCommands(Enum):
    class_info_parse = 'Парсинг информаций о классе 📚'
    class_schedule_parse = 'Парсинг расписаний ⏳'


class UserCommands(Enum):
    start = 'Стартануть бота'
    parseinfo = 'Парсить информацию о классе'
    parseschedule = 'Парсинг расписаний'
