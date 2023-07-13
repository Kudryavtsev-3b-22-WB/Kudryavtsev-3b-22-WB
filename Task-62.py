class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        distance = self.speed * time
        print(f"The robot {self.name} has traveled {distance} units.")


class TrackedRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory


class WheeledRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand




robot1 = Robot("Обычный робот", 10)
robot1.movement(5)  # Вывод: The robot Обычный робот has traveled 50 units.

robot2 = TrackedRobot("Гусеничный робот", 8, "Лес")
robot2.movement(3)  # Вывод: The robot Гусеничный робот has traveled 24 units.
print(f"Territory: {robot2.territory}")  # Вывод: Territory: Лес

robot3 = WheeledRobot("Робот на колесах", 12, "Tesla")
robot3.movement(2)  # Вывод: The robot Робот на колесах has traveled 24 units.
print(f"Car brand: {robot3.car_brand}")  # Вывод: Car brand: Tesla