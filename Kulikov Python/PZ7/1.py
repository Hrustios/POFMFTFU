#Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и русских букв. 
def count_lowercase_letters(string = "Hello, пайтон!"):
    try:
        latin_letters = list("abcdefghijklmnopqrstuvwxyz")  # Латинские строчные буквы
        russian_letters = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")  # Русские строчные буквы

        latin_count = 0
        russian_count = 0

        for char in string:
            if char in latin_letters:
                latin_count += 1
            elif char in russian_letters:
                russian_count += 1

        print(f"Латинских строчных букв: {latin_count}")
        print(f"Русских строчных букв: {russian_count}")
        return latin_count, russian_count
    except Exception:
        print("Ошибка обработки строки.")
        return 0, 0

# Пример вызова
string = input("Введите вашу строку: \n")
count_lowercase_letters(string)
