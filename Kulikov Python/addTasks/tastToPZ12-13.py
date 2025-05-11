from random import randint
from functools import reduce

#В двумерном списке найти максимальный элемент кратный 4

def generate_matrix(rows, cols):
    return list(map(lambda _: list(map(lambda __: randint(0, 10), range(cols))), range(rows)))

def find_max_multiple_of_4(matrix):
    flattened = reduce(lambda acc, row: acc + row, matrix)
    multiples_of_4 = list(filter(lambda x: x % 4 == 0 and x > 0, flattened))
    return reduce(lambda a, b: a if a > b else b, multiples_of_4, None)

def main():
    rows = int(input("Введите количество рядов: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = generate_matrix(rows, cols)
    print("Матрица:")
    print('\n'.join(map(str, matrix)))
    result = find_max_multiple_of_4(matrix)
    print(f"Максимальный элемент, кратный 4: {result}" if result else "Нет подходящих элементов.")

main()
