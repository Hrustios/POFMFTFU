# Сгенерировать двумерный список произвольного размера 
# где каждый следующий элемент строки получается из предыдущего
# с помощью функции преобразования.

import functools
import random

def generate_row(start_value, length, transform):
    return functools.reduce(lambda acc, x: acc + [transform(acc[-1])],range(length - 1),[start_value])

def generate_2d_list(rows, cols, start_gen, transform):
    return list(map(lambda x: generate_row(start_gen(), cols, transform),range(rows)))

def main():
    rows, cols = 5, 5
    table = generate_2d_list(rows, cols, lambda: random.randint(0, 10), lambda x: x + random.randint(1, 10))

    for row in table:
        print(" ".join(map(str,row)))
    print("Каждое следующее число в строке = предыдущее число + случайное число \nНовая строка начинется со случайного числа")
        
main()