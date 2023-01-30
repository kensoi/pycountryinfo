"""
Выполнил Прокофьев А.
Фт-210008
"""

import json

def load_country_info():
    """
    загрузка информации из country_info.json
    """
    
    with open("country_info.json", encoding="utf-8") as json_file: # берём данные из JSON файла
        json_data = json.load(json_file)
        country_info = json_data["data"]

    return country_info


def user_interface(country_info, variant):
    """
    скрипт поиска
    """

    if variant:
        subject_type = input("Выберите тип субъекта [город/государство] >> ").lower()
        
        if subject_type not in ["город", "государство"]:
            print("Некорректный тип субъекта, попробуйте ещё раз")
            return

        if subject_type == "город": # поиск по названию столицы
            subject_type = "capital"
        
        if subject_type == "государство": # поиск по названию государства
            subject_type = "country"

    subject_name = input("Введите название субъекта >> ")

    if subject_name == "выход": # возможность завершить программу
        return 1
    
    try:
        # переключатель лямбда функций (по типу или по наличию)
        expression = (lambda x: x[subject_type].lower() == subject_name.lower()) if variant\
            else (lambda x: subject_name.lower() in [
                x["country"].lower(), 
                x["capital"].lower()])
        
        # поиск по названию
        subject_data = list(filter(expression, country_info))[0]
        print(f"Город \"{subject_data['capital']}\" является столицей государства \"{subject_data['country']}\"")

    except Exception as e: # описание ошибки
        if not variant:
            print("Неизвестный субъект")

        elif subject_type == "capital":
            print("Этот город не является столицей одного из известных государств, либо такого города не существует")

        elif subject_type == "country":
            print("Такого государства не существует либо оно неизвестно программе")


def main():
    """
    Основная функция программы
    """
    country_info = load_country_info() # получение информации из country_info.json
    variant = input("Включить ручной выбор типа субъекта [да/нет] >> ").lower() == "да"

    while True:
        response = user_interface(country_info, variant)

        if response == 1: # пользователь ввёл "выход"
            break


if __name__ == "__main__":
    main()
