class Student:

    def __init__(self, name, lastname, group, grades):
        self.name = name
        self.lastname = lastname
        self.group = group
        self.grades = grades

    def gpa(self):
        return sum(self.grades) / len(self.grades)


student = Student("Кудрявцев", "Евгений", "3b-22-WD", [4, 4, 5, 4])
print(student.gpa())