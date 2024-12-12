#1
n = int(input("Введите верхнее ограничение n (от 1 до 100): "))
if not (1 <= n <= 100):
    print("Ошибка: введено неправильное значение n. Оно должно быть в пределах от 1 до 100.")
else:
    sum_of_cubes = sum(i**3 for i in range(1, n + 1))
    print(f"Сумма кубов чисел от 1 до {n} равна {sum_of_cubes}.")

#2
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i*j:2}', end=' ')
    print()

#3
def rotate_matrix_anticlockwise(matrix):
    transposed = list(zip(*matrix))
    rotated = [row[::-1] for row in transposed]
    
    return rotated
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_matrix = rotate_matrix_anticlockwise(matrix)
for row in rotated_matrix:
    print(row)