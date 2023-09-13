list1 = ['cat', 'elephant', 'dog', 'giraffe', 'mouse']


def get_max_str(lst):
    return max(lst, key=len)


ret = get_max_str(list1)
print(ret)
