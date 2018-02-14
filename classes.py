students = []


class Student:
    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=232):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()


mark = Student("Mark")
andrey = Student(1)
print(students[1])
