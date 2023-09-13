def sum_matrix_diagonal(matrix):
    sum_ = 0
    count = 0
    for row in range(len(matrix)):
        if row == count:
            sum_ += matrix[row][count]
            count += 1
    return sum_


matrix1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
ret = sum_matrix_diagonal(matrix1)
print(ret)

