import requests


query = {
    'text': 'крановщик',
    'per_page': 100
}
response = requests.get('https://api.hh.ru/vacancies', params=query)
result = response.json()
pass

answer = input()
hh_api.get_vacancies_data(answer)


def __lt__(self, other):
    if self.salary and other.salary:

    return self.salary < other.salary

if __name__ == "__main__":
    main()