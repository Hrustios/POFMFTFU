from random import randint
from functools import reduce

def generate_matrix():
    rows = int(input("Введите количество рядов: "))
    cols = int(input("Введите количество столбцов: "))
    return [[randint(0,10) for x in range(cols)] for x in range(rows)]

def find_max_multiple(matrix):
    return reduce(lambda a, b: a if a > b else b,
            filter(lambda x: x > 0 and x % 4 == 0,
            [num for row in matrix for num in row]))

def main():
    matrix = generate_matrix()
    print("Матрица:\n" + '\n'.join(map(str, matrix)))
    print(find_max_multiple(matrix) or "Нет подходящих элементов")

main()