class Student:

    def __init__(self, name, lastname, age, speciality):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.speciality = speciality

    def info(self):
        print("{} - {}, {} лет, {}".format(self.name, self.lastname, self.age, self.speciality))

student = Student("Евгений", "Кудрявцев", 23, "Веб-разработка")
student.info()