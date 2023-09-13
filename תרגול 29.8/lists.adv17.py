import operator
from functools import reduce
from collections import Counter


def count_list(_first_list, second_list_updated_):
    return reduce(operator.add, zip(first_list, second_list_updated_))


first_list = ["father", "kayak", "madam", "Ronaldo", "Noa", "David"]
second_list = ["xavi", "Xman", "banana", "aoN", "madam", "kayak"]
second_list_updated = []
for word in second_list:
    second_list_updated.append(word[::-1])
alternately_list = list(count_list(first_list, second_list_updated))
# now need to find the double words
count_dict = Counter(alternately_list)  # created a dictionary: key = word, value = num of times]
double_words_list = []
for val in count_dict.values():
    if val > 1:
        double_words_list = [k for k, v in count_dict.items() if v == val]  # took the key out
# now need to remove the double word in the smallest index
index_list = []
for word in double_words_list:
    index_ = alternately_list.index(word)
    alternately_list.pop(index_)
print(alternately_list)



















