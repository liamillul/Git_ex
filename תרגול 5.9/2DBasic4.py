from MatrixFuncPrint import print_matrix


def is_guests_list(list1, list2, list3):
    invites_list.append(list1)
    invites_list.append(list2)
    invites_list.append(list3)
    return invites_list


def remove_vip(guest_name):
    for row in ret:
        for name in row:
            if name == guest_name:
                name_to_remove = guest_name
                row.remove(name_to_remove)
    return ret


def friend_to_add(friends_name):
    for row in range(len(ret2)):
        if row == 2:
            name_to_add = friends_name
            ret2[row].append(name_to_add)
    return ret2


invites_list = []
VIP_guests = ["ofir", "bar", "neta"]
family = ["aviram", "ohad"]
friends = ["moti", "liron", "dani"]

ret = is_guests_list(VIP_guests, family, friends)
print_matrix(ret)


guest_to_remove = input("enter the name of the vip guest that can't come: ")
friend_instead = input("enter the name of the friend that will come: ")
ret2 = remove_vip(guest_to_remove)
print_matrix(friend_to_add(friend_instead))


