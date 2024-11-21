#Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать 
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей площади.
def count_squares(a, b):
    try:
        a = int(a)
        b = int(b)
        if a <= 0 or b <= 0:
            raise ValueError("Стороны прямоугольника должны быть натуральными числами.")
        
        squares = 0
        while a > 0 and b > 0:
            if a > b:
                squares += a // b
                a %= b
            else:
                squares += b // a
                b %= a
        return squares
    except ValueError:
        print("Ошибка: стороны прямоугольника должны быть натуральными числами.")
        return None

# Пример вызова:
try:
    A = input("Введите длину стороны A: ")
    B = input("Введите длину стороны B: ")
    result = count_squares(A, B)
    if result is not None:
        print(f"Количество квадратов: {result}")
except Exception:
    print("Произошла ошибка.")
