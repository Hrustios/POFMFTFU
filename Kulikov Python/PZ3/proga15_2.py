#Даны целочисленные координаты точки на плоскости. 
# Если точка совпадает с пачалом координат, то вывести 0.
# Если точка не совпадает с началом координат, по лежит на оси ОХ или ОУ,
# то вывести соответственно 1 или 2. 
# Если точка не лежит на координатных осях, то вывести 3.
try:
    # Ввод координат x и y
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))

    # Проверка расположения точки
    if x == 0 and y == 0:
        print("Точка совпадает с началом координат: 0")
    elif x == 0:
        print("Точка лежит на оси OY: 2")
    elif y == 0:
        print("Точка лежит на оси OX: 1")
    else:
        print("Точка не лежит на координатных осях: 3")

except ValueError: 
    print("Ошибка: Введите корректные целые числа для координат.")
