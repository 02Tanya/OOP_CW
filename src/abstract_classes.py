from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """
    Абстрактный класс для обеспечения получения вакансий с сайта с использованием API.
    """
    def __init__(self, url_get, count_vacancies=50):
        self._url_get = url_get
        self._count_vacancies = count_vacancies

    @abstractmethod
    def get_vacancies(self, vacancy_title):
        pass


class VacancyData(ABC):
    """
    Абстрактный класс для работы с файлом, содержащим выборку вакансий.
    """
    @abstractmethod
    def add_data_to_file(self, vacancy):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def remove_data_from_file(self):
        pass
