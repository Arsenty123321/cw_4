from abc import ABC, abstractmethod
from typing import List

import requests

from config import HH_API_URL, HH_API_MAX_PAGES


class API(ABC):
    """
    Абстрактный класс для работы с api
    """

    @abstractmethod
    def get_vacancies(self, vacancy_name) -> dict:
        pass


class HHAPI(API):
    """
    Класс получения вакансий через API HH
    """

    def __init__(self):
        self.url = HH_API_URL
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'text': '',
            'page': 0,
            'per_page': 100,
            'search_field': 'name',
            "area": 113,
        }
        self.vacancies = []

    def get_vacancies(self, vacancy_name) -> List[dict]:
        """
        Получение списка вакансий
        """
        self.params["text"] = vacancy_name

        while self.params.get('page') != HH_API_MAX_PAGES:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                raise ValueError(f'Ошибка запроса данных: status_code={response.status_code} url={self.url}')
            else:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
        return self.vacancies
