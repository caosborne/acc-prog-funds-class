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
