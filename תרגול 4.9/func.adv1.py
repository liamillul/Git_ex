def make_tuple(measurements, list_):
    list_.append(tuple(measurements))
    return list_


def is_box_size(boxes_lst, boxes_size_list):
    box_size = 1
    for measurements in boxes_lst:
        for i in measurements:
            box_size *= int(i)
        boxes_size_list.append(box_size)
    return boxes_size_list


# closets
closet_num = int(input("how many closets are there: "))
closets = []
for num in range(1, closet_num + 1):
    closet_measurements = input("enter - length width height - of closet" + str(num) + ": ")
    closet_measurements = closet_measurements.split()
    closets = make_tuple(closet_measurements, closets)
# boxes
box_num = int(input("how many boxes are there: "))
boxes = []
for num in range(1, box_num + 1):
    box_measurements = input("enter - length width height - of box" + str(num) + ": ")
    box_measurements = box_measurements.split()
    boxes = make_tuple(box_measurements, boxes)

# now I need to create a function that find which box suits for which closet

right_boxes = []
for num1 in closets:
    for num2 in boxes:
        if num2[0] >= num1[0] and num2[1] >= num1[1] and num2[2] >= num1[2]:
            right_boxes.append(num2)
    if len(right_boxes) == 1:
        print("the box that fits the closet", num1, "is", right_boxes[0])
    elif len(right_boxes) == 0:
        print("the box that fits the closet", num1, "is -1")
    else:
        box_size_list1 = []
        box_size_list_updated = is_box_size(right_boxes, box_size_list1)
        keys = right_boxes
        values = box_size_list1
        res = {keys[i]: values[i] for i in range(len(keys))}
        right_box = min(res)
        print("the box that fits the closet", num1, "is", right_box)
