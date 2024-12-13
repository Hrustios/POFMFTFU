#Дан список А размера N. Вывести его элементы в следующем порядке: А1, АN, A2, AN-1, A3, AN-2, .... 
def custom_order(lst):
    try:
        result = []
        n = len(lst)
        for i in range((n + 1) // 2):
            result.append(lst[i])  # Элемент с начала
            if i != n - i - 1:     # Элемент с конца (если не повторяется)
                result.append(lst[n - i - 1])
        print("Результат:", result)
    except Exception:
        print("Ошибка обработки списка.")

# Пример вызова
lst = [1, 2, 3, 4, 5, 6]
custom_order(lst)
