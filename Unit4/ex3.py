number_of_students = 1  # global variable


def add():
    global number_of_students
    number_of_students = number_of_students + 2  # increment c by 2
    print('Inside the add function ', number_of_students)


add()
print('I\'m outside the add function')
print(number_of_students)
