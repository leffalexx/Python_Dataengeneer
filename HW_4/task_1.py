# Напишите функцию для транспонирования матрицы


def transpose(input_matrix):
    return [[row[i] for row in input_matrix] for i in range(len(input_matrix[0]))]


matrix_to_transpose = [[1, 2, 3],
          [4, 5, 6]]

print(matrix_to_transpose)
transposed = transpose(matrix_to_transpose)
print(transposed)  
