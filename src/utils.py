from config import HH_API_URL
from src.api import HHAPI
from src.saver import JSONworker
from src.vacancy import FromVacancy


def get_vacancies_objects(vacancies: list[dict]) -> list[FromVacancy]:
    """
    Создает список экземпляров класса вакансий.
    """
    return [FromVacancy.create_vacancy(vacancy) for vacancy in vacancies]


def filter_vacancies(vacancies: list[FromVacancy], filter_words: list, salary_range: str, top_n: int)\
        -> list[FromVacancy]:
    """
    Возвращает top_n вакансий отфильтрованных по зарплате в диапазоне salary_range и ключевым словам filter_words.
    """
    filtered_vacancies = []
    # Фильтрация по ключевым словам
    for vac in vacancies:
        if len(filter_words) > 0:
            for w in filter_words:
                if w.lower() in str(vac).lower():
                    filtered_vacancies.append(vac)
                    break
        else:
            filtered_vacancies.append(vac)

    # Фильтрация вакансий по диапазону зарплат
    salary_from, salary_to = [int(value) for value in salary_range.split('-')]
    sorted_vacancies = sorted(list(filter(lambda v: salary_from <= v.salary <= salary_to, filtered_vacancies)),
                              reverse=True)
    if top_n > len(sorted_vacancies):
        top_n = len(sorted_vacancies)
    return sorted_vacancies[:top_n]


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    search_query = input("Введите поисковый запрос: ")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000-150000): ")

    hh_api = HHAPI()
    print(f"\nЗапрос вакансий с {HH_API_URL}. Пожалуйста, подождите...")
    vacancies_data = hh_api.get_vacancies(search_query)

    print(f"Обработка данных...\n\n")
    vacancies_list = get_vacancies_objects(vacancies_data)
    filter_vacancies_list = filter_vacancies(vacancies_list, filter_words, salary_range, top_n)

    json_worker = JSONworker()

    vacancies_count = len(filter_vacancies_list)
    if vacancies_count > 0:
        for vacancy in filter_vacancies_list:
            # Добавление вакансии в файл
            json_worker.add_vacancy(vacancy)
            print(vacancy)
        print(f"Всего найдено: {vacancies_count}")
    else:
        print("\nНе найдено вакансий, удовлетворяющих критериям поиска.")
