#В последовательности на n целых чисел найти и вывести:
# 1.Максимальный среди положительных
# 2.Минимальный среди отрицательных
# 3.Произведение элементов

from random import randint
from functools import reduce

def main():
    n = int(input("Введите колличество чисел последовательности:\n"))
    start = randint(-5,0)
    end = start + n
    _list = [x for x in range(start,end)]
    print(f'Последовательность для обработки: {", ".join(map(str,(_list)))}')

    print("Максимальное число из последовательности:",max(_list))
    print("Минимальное число из последовательности:",min(_list))

    mul_res = reduce(mul,_list)
    mul_res_nn = reduce(mul_nn,_list)

    print("Произведение всех элементов:",mul_res)
    print("Произведение всех элементов, кроме равного нулю:",mul_res_nn)

mul = lambda a, b : a * b

def mul_nn(a,b):
    if a!=0 and b!=0:
        return a * b
    else:
        return a + b
    
main()