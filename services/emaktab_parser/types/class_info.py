from dataclasses import dataclass


@dataclass
class Pupil:
    first_name: str
    last_name: str
    surname: str | None = None

    @property
    def full_name(self) -> str:
        return f'{self.surname} {self.first_name} {self.surname}'


@dataclass
class ClassInfo:
    school_number: int
    pupil_class: str
    academic_start_year: int
    academic_end_year: int
    pupils: list[Pupil]

    @property
    def pupils_count(self) -> int:
        return len(self.pupils)
