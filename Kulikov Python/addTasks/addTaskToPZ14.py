# программа считывает текстовый файл с именем "phone_numbers.txt" и находит все корректные номера телефонов 
# соответствующие формату +7(xxx)xxx-xx-xx или 8(xxx)xxx-xx-xx и выводит их в консоль, каждый на новой строке.
# Обработать отсутствие файла или если он не содержит номеров

# Задача: считать файл "phone_numbers.txt" и найти корректные номера телефонов
# в формате +7(xxx)xxx-xx-xx или 8(xxx)xxx-xx-xx. Каждый найденный номер
# вывести в консоль на новой строке. Учесть отсутствие файла или номеров.

import re

pattern = re.compile(r'(?:\+7|8)\(\d{3}\)\d{3}-\d{2}-\d{2}')

try:
    file = open("phone_numbers.txt", "r", encoding="utf-8")
    summary = file.read()
    variants = pattern.findall(summary)
    
    if variants:
        print("Найденные номера телефонов:")
        for number in variants:
            print(number)
        input()
    else:
        print("В файле нет номеров телефонов в нужном формате.")
        input()
except FileNotFoundError:
    print("Файл 'phone_numbers.txt' не найден.")
    input()
