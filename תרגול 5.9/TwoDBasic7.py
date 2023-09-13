def create_matrix(len_matrix_, matrix_):
    for row in range(len_matrix_):
        row_list = []
        for col in range(len_matrix_):
            row_list.append(0)
        matrix_.append(row_list)
    return matrix_


def print_chessboard(matrix):
    for row in matrix:
        print(row)


def location_queen(row, col):
    row_i = row - 1
    col_i = col - 1
    location_index = [row_i, col_i]
    return location_index


def queen_sign_(matrix, queen_sign, row_index_, col_index_):  # not active yet - need to activate after diagonals
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == col_index_ and row == row_index_:
                matrix[row][col] = queen_sign
    return matrix


def straight_options(matrix, row_index_, col_index_):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == row_index_ or col == col_index_:
                matrix[row][col] = CAN_DIGIT
    return matrix


def diagonals(matrix, row_, col_):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row - col == row_ - col_ or row + col == row_ + col_:
                matrix[row][col] = CAN_DIGIT
    return matrix


# created 8*8 chessboard with 0 in it
chess_board = []
chess_board = (create_matrix(8, chess_board))

QUEEN = "X"
CAN_DIGIT = 1
CANT_DIGIT = 0

row_num = int(input("enter the number of the row: "))
col_num = int(input("enter the number of the col: "))
location_index_list = location_queen(row_num, col_num)
row_index = location_index_list[0]
col_index = location_index_list[1]
# created a new board with all the straight options
ret1 = straight_options(chess_board, row_index, col_index)

# now need to take care of the diagonals, and then activate the queen sign func
ret2 = diagonals(ret1, row_index, col_index)
chess_board_upd = queen_sign_(ret2, QUEEN, row_index, col_index)
print_chessboard(chess_board_upd)
