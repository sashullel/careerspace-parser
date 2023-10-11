from pathlib import Path
from typing import Optional, Sequence

from core_utils.constants import ASSETS_PATH


def get_vacancy_id_from_filepath(path: Path) -> int:
    """
    Extracts the article id from its path
    """
    return int(path.stem.split('_')[0])

class Vacancy:
    """
    Vacancy class implementation.
    Stores info about a vacancy's id, url,
    Title, level of qualification, employer,
    Location, hybrid format, salary and whole description
    """

    def __init__(self, url: Optional[str], vacancy_id: int) -> None:
        self.vacancy_id = vacancy_id
        self.name = ''
        self.level = ''
        self.employer = ''
        self.location = ''
        self.salary_bottom_line = 0
        self.salary_top_line = None
        self.remote = False
        self.hybrid = False
        self.url = url

    def get_info(self) -> dict:
        """
        Gets all meta params
        """
        return {
            'id': self.vacancy_id,
            'Вакансия': self.name,
            'Уровень': self.level,
            'Работодатель': self.employer,
            'Город': self.location,
            'Минимальная зарплата': self.salary_bottom_line,
            'Максимальная зарплата': self.salary_top_line,
            'Удаленно': self.remote,
            'Гибридно': self.hybrid,
            'Ссылка': self.url,
        }

