from func import *

# relevant constant
STARTING_HOUR = 8
DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
days_dict = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5}

amount_of_days = int(input("Enter the amount of days:"))
hours_per_day = int(input("Enter the hours per days:"))
schedule = []

# Initializing the schedule
Lessons = []
schedule = create_matrix(amount_of_days, hours_per_day, schedule)
# The data is inserted:
lesson = input("enter a class- [name of class]_[how many hours the class]_[day]_[starting hour]: ")
while lesson != "done":
    Lessons.append(lesson)
    lesson = input("enter a class- [name of class]_[how many hours the class]_[day]_[starting hour]: ")

# Initial insertion of lessons
# created a matrix that every list in it is a split of different lesson
lessons_out_list = []
flag = "yes"
flags_list_ = []
for class_ in Lessons:
    lesson_split = class_.split("_")
    name_of_lesson = lesson_split[0]
    lesson_duration = lesson_split[1]
    lesson_day = lesson_split[2]
    lesson_hour = lesson_split[3]
    initial_insertion(schedule, lesson_day, lesson_hour, lesson_duration, name_of_lesson, flags_list_,
                      lessons_out_list, days_dict)
    flags_list_ = []

# Final insertion of lessons
lessons_that_still_out = []
final_insertion(lessons_out_list, schedule, flags_list_, lessons_that_still_out)

# now need to print the schedule like I was asked
for i in range(amount_of_days):
    # need to take the key out by the value
    day_name = list(days_dict.keys())[list(days_dict.values()).index(i)]
    print(day_name, ":")
    schedule = np.array(schedule)
    day_index = days_dict[day_name]
    this_day_list = schedule[day_index]
    print(this_day_list)
