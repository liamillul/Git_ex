programming_grade = int(input("enter your programming grade: "))
math_grade = int(input("enter your math grade: "))
coworking_grade = float(input("enter your coworking grade: "))

# conditions to classify the girl
if 0 < programming_grade < 10 and 0 < math_grade < 10 and 0 < coworking_grade < 7.5:
    if programming_grade >= 9 and math_grade >= 9 and coworking_grade >= 6:
        print("CLASS_A")
    elif programming_grade >= 8 and math_grade >= 8 and coworking_grade > 5.5:
        print("CLASS_B")
    elif programming_grade >= 6 and math_grade + coworking_grade >= 10.3:
        print("CLASS_C")
    elif coworking_grade > programming_grade or coworking_grade > math_grade:
        print("CLASS_D")
    else:
        print("maybe next summer")
else:
    print("the grades are not in the suitable range")
