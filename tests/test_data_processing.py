import os
import pytest
from src.data_processing import JSONVacancyData


def test_add_vacancies(json_vacancy_data):
    vacancies = [
        {"title": "Бухгалтер", "salary": 250_000, "city": "Москва"},
        {"title": "Инвестиционный аналитик", "salary": 180_000, "city":
            "Ростов-на-Дону"}
    ]
    json_vacancy_data.add_data_to_file(vacancies)
    assert json_vacancy_data.get_data_from_file() == vacancies


def test_remove_data_from_file(json_vacancy_data):
    vacancies = [
        {"title": "Бухгалтер", "salary": 250_000, "city": "Москва"},
        {"title": "Инвестиционный аналитик", "salary": 180_000, "city":
            "Ростов-на-Дону"}
    ]
    json_vacancy_data.add_data_to_file(vacancies)
    json_vacancy_data.remove_data_from_file()
    assert os.stat(json_vacancy_data.filename).st_size == 0


def test_get_data_from_file_empty(tmpdir):
    temp_file = tmpdir.join("empty_vacancies.json")
    temp_file.write("[]")
    json_vacancy_data = JSONVacancyData(temp_file)
    assert json_vacancy_data.get_data_from_file() == []