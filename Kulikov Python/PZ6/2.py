#Дан целочисленный список размера N, все элементы которого упорядочены (по возрастанию или по убыванию). Найти количество различных элементов в данном списке.
def count_unique(lst):
    try:
        if not lst:  # Проверка на пустой список
            print("Список пуст.")
            return 0
        
        unique_count = 0
        seen = set()  # Множество для отслеживания уже встреченных элементов

        for element in lst:  # Перебор каждого элемента
            if element not in seen:
                unique_count += 1  # Если элемент не встречался, увеличиваем счётчик
                seen.add(element)  # Добавляем элемент в множество

        print("Количество различных элементов:", unique_count)
        return unique_count
    except Exception:
        print("Ошибка обработки списка.")
        return 0

# Пример вызова
lst = [1, 1, 2, 2, 3, 3, 1]
count_unique(lst)
