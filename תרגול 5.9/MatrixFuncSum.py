def sum_matrix(matrix):
    sum_ = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            sum_ += matrix[row][col]
    return sum_
