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
