def is_problem(matrix):
    for row_i in range(len(matrix)):  # every row
        for col_i in range(len(matrix[row_i])):  # every col
            if matrix[row_i][col_i] == "problem":
                screen_index_list = [row_i, col_i]
                screen_index = tuple(screen_index_list)
                faulty_screen_i_list.append(screen_index)
    return faulty_screen_i_list


WORKING_SCREEN = "work"
FAULTY_SCREEN = "problem"
tv = [
    [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
    [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]
]

faulty_screen_i_list = []
print(is_problem(tv))




