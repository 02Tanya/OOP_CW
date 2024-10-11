# import os
# import json
# from src.data_processing import JSONVacancyData
#
#
# def test_add_vacancies(json_vacancy_data):
#     # Список словарей вакансий.
#     vacancies = [
#         {"title": "Программист", "salary": 100_000, "city": "Москва"},
#         {"title": "Аналитик данных", "salary": 120_000, "city":
#             "Санкт-Петербург"}
#     ]
#
#     # Добавляем вакансии в JSON-файл.
#     json_vacancy_data.add_vacancies(vacancies)
#
#     # Читаем данные из файла и проверяем их соответствие добавленным вакансиям.
#     assert json_vacancy_data.get_data_from_file() == vacancies
#
#
# def test_remove_data_from_file(json_vacancy_data):
#     # Список словарей вакансий.
#     vacancies = [
#         {"title": "Программист", "salary": 100_000, "city": "Москва"},
#         {"title": "Аналитик данных", "salary": 120_000, "city":
#             "Санкт-Петербург"}
#     ]
#     json_vacancy_data.add_vacancies(vacancies)
#
#     # Удаляем данные из файла
#     json_vacancy_data.remove_data_from_file()
#
#     # Проверяем пуст ли файл.
#     assert os.stat(json_vacancy_data.filename).st_size == 0
#
#
# def test_get_data_from_file_empty(tmpdir):
#     # Создаём пустой JSON-файл
#     temp_file = tmpdir.join('empty_vacansies.json')
#     temp_file.write('[]')
#
#     # Инициализируем JSONVacancyData пустым файлом
#     json_vacancy_data = JSONVacancyData(temp_file)
#
#     # Проверяем, что список вакансий из пустого файла пустой
#     assert json_vacancy_data.get_data_from_file() == []



