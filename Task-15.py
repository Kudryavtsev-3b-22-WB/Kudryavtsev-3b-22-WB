class Car:

    def __init__(self, brand, model, year, cost):
        self.brand = brand
        self.model = model
        self.year = year
        self.cost = cost

    def info(self):
        print("{} - {}, {}, {}".format(self.brand, self.model, self.year, self.cost))

my_car = Car("Lexus", "Es250", 2019, 4000000)
my_car.info()