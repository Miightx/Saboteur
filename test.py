# Illustration of creating a class
# in Python with input from the user
class Student:
    'A student class'
    stuCount = 0

    # initialization or constructor method of
    def __init__(self):

        # class Student
        self.name = input('enter student name:')
        self.rollno = input('enter student rollno:')
        Student.stuCount += 1

    # displayStudent method of class Student
    def displayStudent(self):
        print("Name:", self.name, "Rollno:", self.rollno)


stu1 = Student()
stu2 = Student()
stu3 = Student()
stu1.displayStudent()
stu2.displayStudent()
stu3.displayStudent()
print('total no. of students:', Student.stuCount)