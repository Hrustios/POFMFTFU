import re

# В исходном текстовом файле (radio_stations.txt) найти все домены из URL-адресов

def extract_domains(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            text = file.read()

        urls = re.findall(r'https?://([a-zA-Z0-9.-]+)', text)
        unique_domains = sorted(set(urls))

        print("Найденные домены:")
        for domain in unique_domains:
            print(domain)
        input()
    except FileNotFoundError:
        res = input("Файл не найден, попробовать ещё раз? [Да/Нет] \n")
        if res.lower() == "да":
            new_name = input("Введите имя файла заново: ")
            extract_domains(new_name)
        elif res.lower() == "нет":
            exit()
        else:
            print("Ответ не распознан")

extract_domains('radio_stations.txt')
