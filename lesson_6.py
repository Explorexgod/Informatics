#1
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
max_in_third_column = max(array[i][2] for i in range(3))
max_in_second_row = max(array[1])
print(f"Максимальное значение в третьем столбце: {max_in_third_column}")
print(f"Максимальное значение во второй строке: {max_in_second_row}")

#2
def transform_array(arr):
    transformed_arr = [[1 if elem > 0 else 0 for elem in row] for row in arr]
    return transformed_arr
m, n = 3, 4
original_array = [
    [-1, 2, -3, 4],
    [5, -6, 7, -8],
    [9, -10, 11, -12]
]
transformed_array = transform_array(original_array)
print("Исходный массив:")
for row in original_array:
    print(row)
print("\nПреобразованный массив:")
for row in transformed_array:
    print(row)

#3
def is_magic_square(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != expected_sum:
            return False
    for j in range(n):
        column_sum = 0
        for i in range(n):
            column_sum += matrix[i][j]
        if column_sum != expected_sum:
            return False

    return True
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
if is_magic_square(matrix):
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")

#4
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
if is_symmetric(matrix):
    print("Матрица симметрична относительно главной диагонали.")
else:
    print("Матрица не симметрична относительно главной диагонали.")

#5
def find_max_and_min_rows(matrix):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    max_sum = -float('inf')
    min_sum = float('inf')
    max_row = None
    min_row = None
    for i in range(rows_count):
        current_sum = sum(matrix[i])
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = matrix[i]
        if current_sum < min_sum:
            min_sum = current_sum
            min_row = matrix[i]
    
    return max_row, max_sum, min_row, min_sum
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
max_row, max_sum, min_row, min_sum = find_max_and_min_rows(matrix)
print(f"Строка с наибольшей суммой: {max_row}, сумма: {max_sum}")
print(f"Строка с наименьшей суммой: {min_row}, сумма: {min_sum}")

#6
n, m = map(int, input().split())
matrix = [list(map(int, input().split()) for _ in range(n))]
for i in range(n):
    min_value = min(matrix[i])
    index = matrix[i].index(min_value)
    if min_value % 2 == 0:
        matrix[i][index] = 0
    else:
        matrix[i][index] = 1
for row in matrix:
    print(' '.join(map(str, row)))