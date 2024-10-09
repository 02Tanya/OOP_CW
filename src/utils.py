import json
from config import operations_path


def load_operations():
    '''Загружает данные из файла .json'''
    with open(operations_path, 'rt') as file:
        file = json.load(file)

        return file
