# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
# Пример использования На входе:
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# На выходе:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def transposed_matrix(matrix: list[list]) -> list[list]:
    transposed_matrix = []
    for i in range(len(matrix[0])):
        line_transp_matrix = []
        for j in range(len(matrix)):
            line_transp_matrix.append(matrix[j][i])
        transposed_matrix.append(line_transp_matrix)
    return transposed_matrix


matrix = [[1, 2, 3, 0],
          [4, 5, 6, 5],
          [7, 8, 9, 1]]
print(transposed_matrix(matrix))
