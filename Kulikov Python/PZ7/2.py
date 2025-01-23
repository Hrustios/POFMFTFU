#Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке знаков препинания
def count_punctuation(string="Привет! Как дела? Это — тестовая строка."):
    try:
        punctuation = set(".,!?;:-—()\"'")  # знаки препинания
        count = 0
        for char in string:
            if char in punctuation:
                count += 1
        print("Количество знаков препинания:", count)
        return count
    except Exception:
        print("Ошибка обработки строки.")
        return 0

string = input("Введите вашу строку: \n")
count_punctuation(string)
