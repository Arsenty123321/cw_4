import json
import os
from abc import ABC, abstractmethod
from config import DATA_DIR, DATA_FILE
from src.vacancy import FromVacancy


class Saver(ABC):
    """
    Абстрактный класс для операций с данными.
    """

    @abstractmethod
    def _read_data(self):
        pass

    @abstractmethod
    def _write_data(self, data):
        pass

    @abstractmethod
    def delete_data(self):
        pass


class JSONworker(Saver):
    """
    Класс для сохранения информации о вакансиях в json-файл.
    """

    def __init__(self):
        """
        При инициализации класса создает директорию и файл с данными, стриает содержимое если файл данных существует
        """
        self.path = os.path.join(DATA_DIR, DATA_FILE)
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self.delete_data()

    def _read_data(self):
        """
        Считывает файл с данными в формате JSON.
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _write_data(self, data):
        """
        Cохраняет данные в формате JSON.
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: FromVacancy):
        """
        Добавляет объекты в файл.
        """
        if not isinstance(vacancy, FromVacancy):
            raise ValueError("Возможно сохранение только объектов типа FromVacancy")
        vacancies_data = self._read_data()
        vacancies_data.append(vacancy.to_dict())
        self._write_data(vacancies_data)

    def delete_data(self):
        """
        Очистка файла с данными
        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump([], file)
