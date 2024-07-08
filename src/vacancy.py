class FromVacancy:
    """
    Класс для работы с вакансиями.
    """
    __slots__ = ['__name', '__salary', '__url', '__area_name', '__requirement']

    def __init__(self, name: str, salary: dict, url: str, area_name: str, requirement: str):
        self.__name = name
        self.__salary = self.__validate_salary(salary)
        self.__url = url
        self.__area_name = self.__validate_data(area_name)
        self.__requirement = self.__validate_data(requirement)

    @property
    def salary(self):
        return self.__salary

    def __str__(self):
        return (
            f"Название: {self.__name}\n"
            f"Зарплата: от {self.__salary}\n"
            f"Город: {self.__area_name}\n"
            f"Ссылка: {self.__url}\n"
            f"Требования: {self.__requirement}\n"
        )

    def __repr__(self):
        return (f'FromVacancy("{self.__name}", {self.__salary}, '
                f'"{self.__url}", "{self.__area_name}", "{self.__requirement}")')

    @staticmethod
    def __validate_salary(salary):
        """
        Метод валидации salary.
        """
        if salary is None:
            return 0
        if isinstance(salary["from"], int) and salary["from"] > 0:
            return salary["from"]
        else:
            return 0

    @staticmethod
    def __validate_data(data):
        """
        Метод валидации остальных полей вакансии.
        """
        if data:
            return data
        else:
            return "Информация не указана."

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        return cls(
            name=vacancy_data["name"],
            salary=vacancy_data["salary"],
            url=vacancy_data["alternate_url"],
            requirement=vacancy_data["snippet"].get("requirement"),
            area_name=vacancy_data["area"].get("name"),
        )

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __lt__(self, other):
        return self.__salary < other.__salary
