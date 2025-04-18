from genlist import matrix_gen 

#В двумерном списке найти суммы элементов каждого столбца и поместить их в новый массив. 
#Заменить элементы влорой строки исходной маптрицы на полученные суммы.
#В двумерном списке найти минимальный элемент в предпоследней строке.
matrix = matrix_gen()
print(f"Сгенерированная матрица:\n{'\n'.join(' '.join(map(str, row)) for row in matrix)}\n")

if len(matrix) > 1:
    el_list = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    matrix[1] = el_list
    print(f"Новая матрица:\n{"\n".join(' '.join(map(str,row)) for row in matrix)}\n")
else: print("Список не является двумерным\n")

if len(matrix) > 1:
    pred_last_row = len(matrix)-2
    print(f"Минимальный элемент из предпоследней строки: {min(matrix[pred_last_row])} ")
