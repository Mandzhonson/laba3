import re
import requests
from bs4 import BeautifulSoup
# СНИЛС в виде ХХХ-ХХХ-ХХХ ХХ

REGULAR = r"^\d{3}\-\d{3}\-\d{3} \d{2}$"
filename = "test_snils.txt"
link = "https://rgup.ru/img/pk_upload/2024/daily/77/Yurisprudentsiya%20(Bakalavr%20ochnaya%20byudzhet)%20(Moskva%202024).html"


def match_snils(snils: str):
    # вернет снилс, если найдет его
    return re.match(REGULAR, snils) is not None


def find_snils_in_file():
    with open(filename, "r") as file:
        snils_arr = []
        for line in file:
            if match_snils(line):
                snils_arr.append(line[:-1])
    return snils_arr


def find_snils_on_site():
    arr_snils = []
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")  # парсим код сайта
    # информация о снилсе хранится в td class=R9C0
    td_class = soup.find_all("td")
    for td in td_class:
        if match_snils(td.text):
            arr_snils.append(td.text)
    return arr_snils


def interface():
    print("1. Найти информацию о снилсах с сайта")
    print("2. Найти снилсы в тестовом файле")
    print("3. Ввести вручную снилс и проверить на правильность")

def print_arr(arr):
    for el in arr:
        print(el)

def main():
    interface()
    choise = input("Введите номер пункта: ")
    match choise:
        case "1":
            print("Считываем информацию с сайта и сразу ищем снилс")
            arr = find_snils_on_site()[:50] # возьмем первые 50 снилсов, так как их на сайте около тысячи
            print_arr(arr)
        case "2":
            print("Считываем информацию с файла и сразу ищем снилс")
            arr = find_snils_in_file()
            print_arr(arr)
        case "3":
            snils = input("Введите номер снилса (Формат: XXX-XXX-XXX XX): ")
            if match_snils(snils):
                print(f"Такой СНИЛС корректен: {snils}")
            else:
                print("Это не СНИЛС, либо вы указали в неправильном формате.")

if __name__ == "__main__":
    main()
