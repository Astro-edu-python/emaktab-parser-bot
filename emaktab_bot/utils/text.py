from services.emaktab_parser.types.class_info import ClassInfo, Pupil


def school_info_print(class_info: ClassInfo) -> str:
    text = (
        f'<b>Информация о школе #️⃣ {class_info.school_number}</b>\n'
        f'<b>Учебный год</b>: {class_info.academic_start_year}\n'
        f'<b>Класс ученика</b>: {class_info.pupil_class}\n'
        f'<b>Кол-во учеников</b>: {class_info.pupils_count}\n'
    )
    return text


def print_pupils_info_text(pupils: list[Pupil]) -> str:
    pupils_text = '\n'.join([
        f'<b>{index}</b>: {pupil.full_name}'
        for index, pupil in enumerate(pupils, start=1)
    ])
    return pupils_text
