from src.data_processing import JSONVacancyData
from src.vacancies_processing import Vacancy


def display_top_vacancies_by_salary() -> None:
    """
    Выводит топ из выбранного количества вакансий по зарплате.
    :return: None
    """
    while True:
        try:
            number_vacancies = int(input("Введите число вакансий для вывода в топ: "))
            break
        except ValueError:
            print("Не корректный ввод. Введите количество вакансий цифрами")
            continue
    vacancies_sort = Vacancy.sort_the_list(Vacancy.all)
    if number_vacancies > len(Vacancy.all):
        number_vacancies = len(Vacancy.all)
    print(f"Топ {number_vacancies} вакансий по зарплате: ")
    Vacancy.print_formatted_vacancies_list(vacancies_sort, number_vacancies)


def filters_and_display_vacancies() -> None:
    """
    Фильтрует вакансии по городу/зарплате и выводит результат пользователю.
    :return: None
    """
    param_number = input(
        "Выберите параметр фильтрации вакансий: \n1 - город " "\n2 - зарплата\n"
    )
    if param_number == "1":
        user_city = input("Введите название города:\n")
        vacancies_city = Vacancy.filtering_vacancies_by_city(user_city)
        if vacancies_city:
            Vacancy.print_formatted_vacancies_list(vacancies_city)
            user_input = input(
                "Сохранить выбранные вакансии в файл\n1 - " "да\nEnter - нет\n"
            )
            if user_input == "1":
                JSONVacancyData().add_data_to_file(vacancies_city)
                print("Вакансии сохранены в файл")
        else:
            print("По вашему запросу ничего не найдено")

    elif param_number == "2":
        while True:
            try:
                user_salary = int(input("Введите минимальный уровень зарплаты:\n"))
                break
            except ValueError:
                print("Не корректный ввод. Введите ожидаемую зарплату цифрами")
                continue
        vacancy_salary = Vacancy.filtering_vacancies_by_salary(user_salary)
        if vacancy_salary:
            Vacancy.print_formatted_vacancies_list(vacancy_salary)
            user_input = input(
                "Сохранить выбранные вакансии в файл\n1 - " "да\nEnter - нет\n"
            )
            if user_input == "1":
                JSONVacancyData().add_data_to_file(vacancy_salary)
                print("Вакансии сохранены в файл")
        else:
            print("По вашему запросу ничего не найдено")
    else:
        print("Не корректный ввод")
