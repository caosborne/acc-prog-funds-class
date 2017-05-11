# The student class file was called studentInfo.py

class StudentInfo:

    def __init__(self, name, studentID, GPA, expGrade):
        self.__name = name
        self.__studentID = studentID
        self.__GPA = GPA
        self.__expGrade = expGrade

    def set_name(self, name):
        self.__name = name

    def set_studentID(self, studentID):
        self.__studentID = studentID

    def set_GPA(self, GPA):
        self.__GPA = GPA

    def set_expGrade(self, expGrade):
        self.__expGrade = expGrade

    def get_name(self):
        return self.__name

    def get_studentID(self):
        return self.__studentID

    def get_GPA(self):
        return self.__GPA

    def get_expGrade(self):
        return self.__expGrade

    def __str__(self):
        return "Name: " + self.__name + \
        "\nStudent ID: " + self.__studentID + \
        "\nGPA: " + self.__GPA + \
        "\nExpected Grade: " + self.__expGrade


# The student list file was called student_list.py

import studentInfo

def main():
    students = make_list()

    print('Here is the data you entered:')
    display_list(students)


def make_list():
    student_list = []

    print('Enter the data for the five students.')
    for count in range(1, 6):
        print('Student info ' + str(count) + ':')
        name = input('Enter the students name: ')
        studentID = input('Enter the students ID number: ')
        GPA = input('Enter the students GPA: ')
        expGrade = input('Enter the students expected grade: ')
        print()

        student = studentInfo.StudentInfo(name, studentID, GPA, expGrade)

        student_list.append(student)

    return student_list

def display_list(student_list):
    for item in student_list:
        print(item.get_name())
        print(item.get_studentID())
        print(item.get_GPA())
        print(item.get_expGrade())
        print()

main()
