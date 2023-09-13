name1 = "CPU percentage"
name2 = "RAM percentage"
name3 = "Disk usage percentage"
names = [name1, name2, name3]


def if_deviation(percentage, name):
    if percentage > 80:
        return name + " " + "exceeded 80%. its current value is" + " " + str(percentage) + "%"


def nic_not_up(dict_, values_list_):
    for nic_stats in values_list_:  # tuple
        nic_check = nic_stats[0]
        if nic_check is False:
            name_list = [k for k, v in dict_.items() if v == nic_stats]
            if len(name_list) > 1:
                for val1 in name_list:
                    name_ = val1
                    print("NIC", name_, "is not up")
                break
            else:
                name_ = name_list
            print("NIC", name_, "is not up")


def speed_of_nic(dict_, speed_list_):
    tuples_list = dict_.values()
    for value in tuples_list:
        speed = value[2]
        speed_list_.append(speed)
    keys_list = list(dict_.keys())
    speed_dict_ = dict(zip(keys_list, speed_list_))
    return speed_dict_
