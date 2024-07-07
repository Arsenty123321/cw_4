from src.vacancy import FromVacancy


def get_vacancies_objects(vacancies: list[dict]) -> list[FromVacancy]:
    """
    Создает список экземпляров класса вакансий.
    """
    return [FromVacancy.create_vacancy(vacancy) for vacancy in vacancies]


def sort_vacancies(vacancies: list[FromVacancy]) -> list[FromVacancy]:
    """
    Возвращает отсортированный по зарплате список экземпляров класса вакансий.
    """
    return sorted(vacancies)
