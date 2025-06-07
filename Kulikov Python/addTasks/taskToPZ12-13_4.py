from random import randint

# В двумерном списке найти минимальный элемент в предпоследней строке

def generate_matrix(rows, cols):
    return [[randint(1, 20) for x in range(cols)] for x in range(rows)]

def find_min(matrix):
    if len(matrix) < 2:
        return None
    return min(matrix[-2])

def main():
    N = int(input("Введите количество рядов и столбцов: "))
    matrix = generate_matrix(N, N) 
    print("Матрица:")
    for row in matrix:
        print(" ".join(map(str,row)))
    result = find_min(matrix)
    if result is not None:
        print(f"Минимальный элемент в последней строке: {result}")
    else:
        print("Недостаточно строк в матрице для выполнения условия.")

main()
