from src.data_processing import JSONVacancyData
from src.vacancies_processing import Vacancy


def display_top_vacancies_by_salary():
    '''Выводит список из выбранного количества вакансий по уменьшению заработной платы'''
    while True:
        try:
            number_vacancies = int(input("Какое количество вакансий необходимо вывести?"))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите количество вакансий числом.")
            continue
    vacancies_sort = Vacancy.sort_the_list(Vacancy.all)
    if number_vacancies > len(Vacancy.all):
        number_vacancies = len(Vacancy.all)
    print(f"Топ {number_vacancies} вакансий по заработной плате: ")
    Vacancy.print_formatted_vacancies_list(vacancies_sort, number_vacancies)


def filter_vacancies_city():
    '''Фильтрует вакансии по городу'''
    user_city = input("Пожалуйста, ведите название города с заглавной буквы:\n")
    vacancies_city = Vacancy.filtering_vacancies_by_city(user_city)
    if vacancies_city:
        Vacancy.print_formatted_vacancies_list(vacancies_city)
        user_input = input("Сохранить текущий список вакансий в файл?\n1 - да\n2 - нет\n")
        if user_input == "1":
            JSONVacancyData().add_data_to_file(vacancies_city)
            print("Вакансии сохранены в файл")
    else:
        print("По вашему запросу ничего не найдено")


def filter_vacancies_salary():
    '''Фильтрует вакансии по заработной плате'''
    while True:
        try:
            user_salary = int(input("Пожалуйста, введите минимальный уровень заработной платы:\n"))
            break
        except ValueError:
            print("Некорректный ввод. пожалуйста, введите нижний порог заработной платы числом:")
            continue
    vacancy_salary = Vacancy.filtering_vacancies_by_salary(user_salary)
    if vacancy_salary:
        Vacancy.print_formatted_vacancies_list(vacancy_salary)
        user_input = input("Сохранить выбранные вакансии в файл\n1 - да\n2 - нет\n")
        if user_input == "1":
            JSONVacancyData().add_data_to_file(vacancy_salary)
            print("Вакансии сохранены в файл")
    else:
        print("По Вашему запросу ничего не найдено")
