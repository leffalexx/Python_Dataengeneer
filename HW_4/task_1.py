# 1. Напишите функцию для транспонирования матрицы


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


matrix = [[1, 2, 3], 
          [4, 5, 6]]

print(matrix)
transposed = transpose(matrix)
print(transposed)  
