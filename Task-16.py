class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print("Кошка по имени {}, {} лет, цвет {}".format(self.name, self.age, self.color))


my_cat = Cat("Кнопка", 3, "Серый")
my_cat.info()