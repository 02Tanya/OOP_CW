from time import sleep
from src.hh_vacancies_api import HHVacancyAPI
from src.data_processing import JSONVacancyData
from src.utils import display_top_vacancies_by_salary, filters_and_display_vacancies
from src.vacancies_processing import Vacancy


def user_search():
    """
    Функция для отображения вакансий в соответствии с критериями пользователя.
    """
    while True:
        vacancy_title = input(
            "Пожалуйста, введите ключевое слово для поиска вакансий: \n"
        )
        if not HHVacancyAPI().get_vacancies(vacancy_title):
            print(
                "По вашему запросу ничего не найдено. Попробуйте изменить параметры запроса."
            )
            continue
        else:
            break
    Vacancy.instance_from_list(vacancy_title)
    print(f"По вашему запросу --{vacancy_title}-- получен список вакансий.")

    while True:
        print("\u001b[36m")
        sleep(1)
        user_input = input(
            "Вы можете сделать следующее:\n"
            "1 - Вывести список найденных вакансий;\n"
            "2 - Сохранить список вакансий в файл;\n"
            "3 - Вывести топ N вакансий по заработной плате;\n"
            "4 - Ввести дополнительные данные для фильтрации вакансий\n"
            "5 - Вывести информацию о вакансиях из файла\n"
            "6 - Удалить информацию о вакансиях из файла\n"
            "7 - Новый поиск\n"
            "8 - Выход\n"
            "\nУкажите номер выбранного Вами действия: "
        )
        print("\u001b[0m")

        if user_input == "1":
            Vacancy.print_formatted_vacancies_list(Vacancy.all)
            continue
        elif user_input == "2":
            JSONVacancyData().add_data_to_file(Vacancy.all)
            print("Вакансии сохранены в файл.")
        elif user_input == "3":
            display_top_vacancies_by_salary()
        elif user_input == "4":
            filters_and_display_vacancies()
        elif user_input == "5":
            vacancies_from_file = JSONVacancyData().get_data_from_file()
            Vacancy.print_formatted_vacancies_list(vacancies_from_file)
        elif user_input == "6":
            JSONVacancyData().remove_data_from_file()
            print("Информация о вакансиях удалена.")
        elif user_input == "7":
            user_search()
            break
        elif user_input == "8":
            print("Работа программы завершена. Будем рады снова помочь Вам с поиском:)")
            break
        else:
            print("Некорректный ввод, попробуйте еще раз.")
            break


if __name__ == "__main__":
    print("\u001b[36m")
    print(
        "* * * Добрый день! Вас приветствует помощник в подборе вакансий. * * *\n "
        "      -------------------------------------------------------"
    )
    print("\u001b[0m")
    user_search()
