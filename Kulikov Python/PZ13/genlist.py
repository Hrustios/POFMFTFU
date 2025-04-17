from random import randint

def matrix_gen(x=0):
    rows = int(input("Введите количество рядов: "))
    cols = int(input("Введите количество элементов в каждом ряду: "))
    max_value_one_element = int(input("Введите максимальное значение для элемента списка: "))
    matrix = [[randint(0,max_value_one_element) for x in range(cols)] for x in range(rows)]
    return matrix
