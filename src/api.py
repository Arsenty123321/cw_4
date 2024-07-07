from abc import ABC, abstractmethod

import requests

from config import HH_API_URL


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
        self.params = {
            'text': '',
            "per_page": 100,
            "search_field": "name",
        }

    def get_vacancies(self, vacancy_name) -> dict:
        """
        Получение списка вакансий
        """
        self.params["text"] = vacancy_name

        response = requests.get(self.url, params=self.params)
        if response.status_code != 200:
            raise ValueError(f'Ошибка запроса данных: status_code={response.status_code} url={self.url}')
        else:
            return response.json()['items']


if __name__ == '__main__':
    hh = HHAPI()
    data = hh.get_vacancies("python")
    print(data)
