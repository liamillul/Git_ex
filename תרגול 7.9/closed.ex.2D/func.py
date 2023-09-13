import numpy as np


def create_matrix(days, hours, matrix):
    for row in range(days):
        row_list = []
        for col in range(hours):
            row_list.append("free")
        matrix.append(row_list)
    return matrix


def initial_insertion(matrix, day, hour, duration, name, flags_list, lessons_out_list_, days_dict_):
    schedule1 = np.array(matrix)
    day_index = days_dict_[day]
    this_day_list = schedule1[day_index]
    starting_index = int(hour) - 8
    ending_forloop = starting_index + int(duration)
    for i in range(starting_index, ending_forloop):
        if this_day_list[i] == "free":
            flag_ = "yes"
            flags_list.append(flag_)
        else:
            flag_ = 0
            flags_list.append(flag_)
    # checked if all the vals in flags list are strings
    if all([isinstance(val, str) for val in flags_list]):
        for i in range(starting_index, ending_forloop):
            matrix[day_index][i] = name
    else:
        lessons_out_list_.append(name + "_" + duration + "_" + day + "_" + hour)
    return matrix, lessons_out_list_


def final_insertion(lessons_out_lst, matrix, flags_list, lessons_still_out):
    for i1 in range(len(lessons_out_lst)):
        lesson_split = lessons_out_lst[i1].split("_")
        name = lesson_split[0]
        # run on the schedule
        for day_ in matrix:
            day_index = matrix.index(day_)
            for hour_ in day_:
                if hour_ == "free":
                    flag_ = "yes"
                    flags_list.append(flag_)
                else:
                    flag_ = 0
                    flags_list.append(flag_)
            # checked if all the vals in flags list are strings
            if all([isinstance(val, str) for val in flags_list]):
                for i in range(len(day_)):
                    matrix[day_index][i] = name
            else:
                flags_list = []
                continue
            return matrix
