from MatrixFuncPrint import print_matrix


def location_submarine(row, col):
    row_ = row - 1
    col_ = col - 1
    location_index = [row_, col_]
    return location_index


def input_check(parameter, guess):
    while guess < 1 or guess > 5:
        guess = int(input("try again. enter the" + " " + parameter + " " + "number: "))
    return guess


def check_guess1(index_list_, _count_, _flag_):
    if index_list_ == [2, 0] or index_list_ == [3, 0] or index_list_ == [4, 0]:
        _count_ += 1
        _flag_ = True
        print("you hit the submarine! it took you", _count_, "try")
        exit()
    else:
        _flag_ = False
        check_guess2(updated_index_list, count, _flag_)


def check_guess2(index_list, count_, flag_):
    while not flag_:
        guess_list_new = []
        guess_new = input("try again. enter the your guess- [row, col]: ")
        split_guess = guess_new.split()
        for x in split_guess:
            guess_list_new.append(x)
        count_ += 1
        guess_row_new = int(guess_list_new[0])
        guess_col_new = int(guess_list_new[1])
        index_list = location_submarine(guess_row_new, guess_col_new)
        check_guess1(index_list, count_, flag)
    return index_list, count_


# main code
SUBMARINE = 'X'
EMPTY = 'O'
board = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY],
    [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY],
    [SUBMARINE, EMPTY, EMPTY, EMPTY, EMPTY]
]
# PART A
guess_row = int(input("enter the row number: "))
guess_col = int(input("enter the column number: "))
index_submarine_list = location_submarine(guess_row, guess_col)
row_i = index_submarine_list[0]
col_i = index_submarine_list[1]
ROW = "row"
COL = "column"
# # input check
# guess_row_valid = input_check(ROW, guess_row)
# guess_col_valid = input_check(COL, guess_col)
# updated_index_list = location_submarine(guess_row_valid, guess_col_valid)
# # row_i_valid = updated_index_list[0]
# # col_i_valid = updated_index_list[1]
# count = 0
# flag = False
# # now check if the guess is true
# check_guess1(updated_index_list, count, flag)

# PART B
guess_row2 = int(input("enter the row number you want to strike: "))
guess_col2 = int(input("enter the column number you want to strike: "))
# turn into index
index_submarine_list2 = location_submarine(guess_row2, guess_col2)
row_i2 = index_submarine_list2[0]
col_i2 = index_submarine_list2[1]
# input check
guess_row_valid2 = input_check(ROW, guess_row2)
guess_col_valid2 = input_check(COL, guess_col2)

count = 0


def is_strike(matrix, _index_list_, row_index, col_index, count_):
    if _index_list_ == [2, 0] or _index_list_ == [3, 0] or _index_list_ == [4, 0]:
        _flag_ = True
        row = row_index
        col = col_index
        matrix[row][col] = "S"
        print_matrix(matrix)
        print("you waisted", count_, "strikes")
    else:
        _flag_ = False
        more_guess(_index_list_, _flag_, count_)


def more_guess(index_list_, flag_, count_):
    while not flag_:
        guess_list_new2 = []
        guess_new2 = input("try again. enter the your guess- [row, col]: ") # after this need input check
        split_guess = guess_new2.split()
        for x in split_guess:
            guess_list_new2.append(x)
        count_ += 1
        guess_row_new2 = int(guess_list_new2[0])
        guess_col_new2 = int(guess_list_new2[1])
        index_list_ = location_submarine(guess_row_new2, guess_col_new2)
        row_i2_new = index_list_[0]
        col_i2_new = index_list_[1]
        is_strike(board, index_list_, row_i2_new, col_i2_new, count_)
    return index_list_, count_


is_strike(board, index_submarine_list2, row_i2, col_i2, count)
