#В последовательности на n целых чисел найти и вывести:
# 1.Максимальный среди положительных
# 2.Минимальный среди отрицательных
# 3.Произведение элементов

from random import randint
from functools import reduce

def main():
    _list = [x for x in range(randint(-100,0),randint(0,100))]

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