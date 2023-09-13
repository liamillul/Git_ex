from MatrixFuncPrint import print_matrix


def create_matrix(len_matrix_, matrix_):
	for row in range(len_matrix_):
		row_list = []
		for col in range(len_matrix_):
			row_list.append(0)
		matrix_.append(row_list)
	return matrix_


def row_minus_col():
	for row in range(len(matrix)):
		for col in range(len_matrix):
			if row - col >= 0:
				result = row - col
				matrix[row][col] = result
	return matrix


len_matrix = int(input("enter the length of the matrix: "))
matrix = []
create_matrix(len_matrix, matrix)
row_minus_col()
print_matrix(matrix)


