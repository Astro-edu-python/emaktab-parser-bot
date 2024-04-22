import requests
from celery import Task
from undetected_chromedriver import Chrome

from config import TELEGRAM_BOT_API_URL
from .celery import app
from services.emaktab_parser.clicker import EMaktabClicker
from services.emaktab_parser.core import EmaktabManager
from ...utils.text import print_pupils_info_text, school_info_print


@app.task(bind=True)
def parse_week_lessons(
    self: Task, bot_token: str, emaktab_login: str, emaktab_password: str,
    chat_id: int
):
    emaktab_clicker = EMaktabClicker(
        Chrome(headless=True),
        emaktab_login,
        emaktab_password
    )
    manager = EmaktabManager(emaktab_clicker)
    schedule = manager.parse_week_lessons()
    response_text = (
        f'<b>Результат задачи {self.request.id}</b>'
        f'\nРасписание уроков по датам '
        f'{schedule.date_start.date()}-{schedule.date_end.date()}\n'
        f'Кол-во уроков на неделю: {schedule.lessons_count}'
    )
    for day_lessons in schedule.lessons:
        today_first_lesson = day_lessons[0]
        lessons_day = today_first_lesson.start_date.date()
        day_lessons_txt: list[str] = []
        for lesson in day_lessons:
            text = (
                f'<b>Предмет {lesson.name}(Учитель {lesson.teacher})</b>\n'
                f'Время проведения: '
                f'{lesson.start_date.time()}-{lesson.end_date.time()}'
            )
            day_lessons_txt.append(text)
        response_text += (
            f'\n\nУроки по дате {lessons_day}\n' + '\n'.join(day_lessons_txt)
        )
    requests.get(
        f'{TELEGRAM_BOT_API_URL}{bot_token}/sendMessage',
        params={
            'chat_id': chat_id,
            'text': response_text,
            'parse_mode': 'HTML',
        }
    )


@app.task(bind=True)
def parse_week_lessons(
    self: Task, bot_token: str, emaktab_login: str, emaktab_password: str,
    chat_id: int
):
    emaktab_clicker = EMaktabClicker(
        Chrome(headless=True),
        emaktab_login,
        emaktab_password
    )
    manager = EmaktabManager(emaktab_clicker)
    class_info = manager.parse_class_info()
    pupils_text = print_pupils_info_text(class_info.pupils)
    response = (
        f'<b>Результат задачи {self.request.id}</b>' +
        school_info_print(class_info) +
        f'<b>Ученики</b>:\n{pupils_text}'
    )
    requests.get(
        f'{TELEGRAM_BOT_API_URL}{bot_token}/sendMessage',
        params={
            'chat_id': chat_id,
            'text': response,
            'parse_mode': 'HTML',
        }
    )
