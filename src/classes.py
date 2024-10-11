from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """
    Абстрактный класс, для работы с API сайтов с вакансиями.
    """

    def __init__(self, url, count_vacancies=50):
        self._url = url
        self._count_vacancies = count_vacancies

    @abstractmethod
    def get_vacancies(self, vacancy_title):
        pass