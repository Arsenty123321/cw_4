class FromVacancy:
    """
    Класс для работы с вакансиями.
    """
    __slots__ = ['__name', '__salary_from', '__url', '__requirement']

    def __init__(self, name: str, salary_from: int, url: str, requirement: str):
        self.__name = name
        self.__salary_from = self.__validate_salary(salary_from)
        self.__url = url
        self.__requirement = requirement

    @property
    def salary_from(self):
        return self.__salary_from

    def __str__(self):
        return (
            f"Название: {self.__name}\n"
            f"Зарплата: от {self.__salary_from}\n"
            f"Ссылка: {self.__url}\n"
            f"Требования: {self.__requirement}\n"
        )

    def __repr__(self):
        return f'FromVacancy("{self.__name}", {self.__salary_from}, "{self.__url}", "{self.__requirement}")'

    @staticmethod
    def __validate_salary(sallary):
        """
        Метод валидации salary.
        """
        return 0 if sallary < 0 else sallary

    @classmethod
    def create_vacancy(cls, vacancy_data: dict):
        return cls(
            name=vacancy_data["name"],
            salary_from=vacancy_data["salary_from"],
            url=vacancy_data["url"],
            requirement=vacancy_data["requirement]"],
        )

    def __gt__(self, other):
        return self.__salary_from > other.__salary_from

    def __lt__(self, other):
        return self.__salary_from < other.__salary_from
