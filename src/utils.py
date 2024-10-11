# import json
# from config import operations_path
#
#
# def load_operations():
#     '''Загружает данные из файла .json'''
#     with open(operations_path, 'rt') as file:
#         file = json.load(file)
#
#         return file


import json
from json import JSONDecodeError
from src.vacancy_data import VacancyData


class JSONVacancyData(VacancyData):
    """
    Класс для работы с JSON файлом.
    """
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def add_data_to_file(self, vacancies) -> None:
        """
        Записывает найденные вакансии в файл.
        :param vacancies: Список вакансий
        :return: None
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def get_data_from_file(self):
        """
        Получает информацию о вакансиях из json-файла.
        :return: Список вакансий. Если файл пустой - пустой список
        """
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                json_file = json.load(file)
                return json_file
        except JSONDecodeError:
            return []

    def remove_data_from_file(self) -> None:
        """
        Удаляет из json-файла данные о вакансиях.
        :return: None
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.seek(0)
            file.truncate()








from src.json_vacancy_data import JSONVacancyData
from src.vacancy import Vacancy


def display_top_vacancies_by_salary() -> None:
    """
    Выводит топ из выбранного количества вакансий по зарплате.
    :return: None
    """
    while True:
        try:
            number_vacancies = int(
                input('Введите число вакансий для вывода в топ: ')
                )
            break
        except ValueError:
            print('Не корректный ввод. Введите количество вакансий цифрами')
            continue
    vacancies_sort = Vacancy.sort_the_list(Vacancy.all)
    if number_vacancies > len(Vacancy.all):
        number_vacancies = len(Vacancy.all)
    print(f'Топ {number_vacancies} вакансий по зарплате: ')
    Vacancy.print_formatted_vacancies_list(vacancies_sort, number_vacancies)


def filters_and_display_vacancies() -> None:
    """
    Фильтрует вакансии по городу/зарплате и выводит результат пользователю.
    :return: None
    """
    param_number = input(
        'Выберите параметр фильтрации вакансий: \n1 - город '
        '\n2 - зарплата\n'
        )
    if param_number == '1':
        user_city = input('Введите название города:\n')
        vacancies_city = Vacancy.filtering_vacancies_by_city(user_city)
        if vacancies_city:
            Vacancy.print_formatted_vacancies_list(vacancies_city)
            user_input = input(
                'Сохранить выбранные вакансии в файл\n1 - '
                'да\nEnter - нет\n'
                )
            if user_input == '1':
                JSONVacancyData().add_data_to_file(vacancies_city)
                print('Вакансии сохранены в файл')
        else:
            print('По вашему запросу ничего не найдено')

    elif param_number == '2':
        while True:
            try:
                user_salary = int(
                    input('Введите минимальный уровень зарплаты:\n'))
                break
            except ValueError:
                print('Не корректный ввод. Введите ожидаемую зарплату цифрами')
                continue
        vacancy_salary = Vacancy.filtering_vacancies_by_salary(user_salary)
        if vacancy_salary:
            Vacancy.print_formatted_vacancies_list(vacancy_salary)
            user_input = input(
                'Сохранить выбранные вакансии в файл\n1 - '
                'да\nEnter - нет\n'
                )
            if user_input == '1':
                JSONVacancyData().add_data_to_file(vacancy_salary)
                print('Вакансии сохранены в файл')
        else:
            print('По вашему запросу ничего не найдено')
    else:
        print('Не корректный ввод')









import datetime
import json

from src.api.hh_vacancy_api import HHVacancyAPI


class Vacancy:
    """
    Класс для работы с вакансиями.
    """
    all = []

    def __init__(self, title, url, salary, salary_currency, date, city):
        self.title = title
        self.url = url
        self.salary = salary
        self.salary_currency = salary_currency
        self.date = date
        self.city = city
        self.all.append(self.__dict__)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_vacancy):
        self.__title = title_vacancy

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url_vacancy):
        self.__url = url_vacancy

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary_vacancy):
        self.__salary = salary_vacancy

    @property
    def salary_currency(self):
        return self.__salary_currency

    @salary_currency.setter
    def salary_currency(self, salary_currency_vacancy):
        self.__salary_currency = salary_currency_vacancy

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date_vacancy):
        self.__date = date_vacancy

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city_vacancy):
        self.__city = city_vacancy

    def __str__(self):
        return (f'Вакансия: {self.title}, зарплата до {self.salary} '
                f'{self.salary_currency}, дата публикации: {self.date}, '
                f'город: {self.city}, url: {self.url}')

    def __gt__(self, other):
        return int(self.salary) > int(other.salary)

    def __ge__(self, other):
        return int(self.salary) >= int(other.salary)

    @classmethod
    def instance_from_list(cls, vacancy_title) -> None:
        """
        Метод класса инициализирующий экземпляры класса данными из списка.
        :param vacancy_title: Название вакансии
        :return:
        """
        hh_vacancies = HHVacancyAPI().get_vacancies(vacancy_title)
        for hh_vacancy in hh_vacancies:
            title = hh_vacancy['name']
            url = hh_vacancy['alternate_url']
            if hh_vacancy['salary']:
                salary = hh_vacancy['salary']['from']
                salary_currency = hh_vacancy['salary']['currency']
            else:
                salary = None
                salary_currency = None
            date = datetime.datetime.strptime(
                hh_vacancy['published_at'], '%Y-%m-%dT%H:%M:%S+%f'
                ).strftime(
                "%d.%m.%Y"
            )
            city = hh_vacancy['area']['name']
            cls(title, url, salary, salary_currency, date, city)

    @classmethod
    def instance_from_json(cls, filename='../vacancies.json') -> None:
        """
        Метод класса инициализирующий экземпляр класса данными из json-файла.
        :param filename: Название файла
        :return: None
        """
        cls.all = []
        try:
            with open(filename, 'rt', encoding='utf-8') as file:
                data = json.load(file)
                for line in data:
                    cls(line["_Vacancy__title"], line["_Vacancy__url"],
                        line["_Vacancy__salary"], line[
                            "_Vacancy__salary_currency"],
                        line["_Vacancy__date"], line["_Vacancy__city"])
        except FileNotFoundError:
            print('Отсутствует файл для чтения')

    @classmethod
    def filtering_vacancies_by_city(cls, city) -> list:
        """
        Метод класса фильтрующий список вакансий по городу
        :param city: Город
        :return: Список вакансий из указанного города
        """
        vacancies_city = []
        vacancies = cls.all
        for vacancy in vacancies:
            if vacancy['_Vacancy__city'] == city:
                vacancies_city.append(vacancy)
            return vacancies_city

    @classmethod
    def filtering_vacancies_by_salary(cls, salary) -> list:
        """
        Метод класса фильтрующий список вакансий по зарплате.
        :param salary: Минимальная зарплата для вывода
        :return: Список вакансий с зарплатой большей или равной указанной
        """
        vacancies_salary = []
        vacancies = Vacancy.filters_the_list(Vacancy.all)
        for vacancy in vacancies:
            if vacancy["_Vacancy__salary"] >= salary:
                vacancies_salary.append(vacancy)
            else:
                vacancies_salary = []
        return vacancies_salary

    @staticmethod
    def sort_the_list(vacancies) -> list:
        """
        Статический метод, который сортирует список вакансий по зарплате.
        :param vacancies: Список вакансий
        :return: Отсортированный список вакансий
        """
        vacancies_filter = Vacancy.filters_the_list(vacancies)
        vacancies_sort = sorted(vacancies_filter, key=lambda s: s[
            "_Vacancy__salary"], reverse=True)
        return vacancies_sort

    @staticmethod
    def filters_the_list(all_vacancies):
        """
        Статический метод, который фильтрует список вакансий по зарплате.
        :param all_vacancies: Список вакансий
        :return: Список содержащий те вакансии, где указана зарплата в RUR
        """
        vacancies = []
        for vacancy in all_vacancies:
            if vacancy.get("_Vacancy__salary") is not None and vacancy.get(
                    "_Vacancy__salary_currency") == "RUR":
                vacancies.append(vacancy)
        return vacancies

    @staticmethod
    def print_formatted_vacancies_list(list_vacancies, number_vacancies=None) -> None:
        """
        Печатает данные о вакансиях для пользователя
        :param list_vacancies: Список вакансий
        :param number_vacancies: Количество вакансий для вывода
        :return: None
        """
        if not list_vacancies:
            print('В файле отсутствуют данные о вакансиях')
        else:
            if number_vacancies is None or number_vacancies > len(
                    list_vacancies
                    ):
                number_vacancies = len(list_vacancies)
            for index in range(number_vacancies):
                if list_vacancies[index]['_Vacancy__salary']:
                    print(
                        f"Профессия: {list_vacancies[index]['_Vacancy__title']}, зарплата до "
                        f"{list_vacancies[index]['_Vacancy__salary']}"
                        f" {list_vacancies[index]['_Vacancy__salary_currency']}, дата публикации: "
                        f"{list_vacancies[index]['_Vacancy__date']}, город: {list_vacancies[index]['_Vacancy__city']}, "
                        f"url: {list_vacancies[index]['_Vacancy__url']}"
                    )
                else:
                    print(
                        f"Профессия: {list_vacancies[index]['_Vacancy__title']}, зарплата не указана, дата публикации: "
                        f"{list_vacancies[index]['_Vacancy__date']}, город: {list_vacancies[index]['_Vacancy__city']}, "
                        f"url: {list_vacancies[index]['_Vacancy__url']}"
                    )
