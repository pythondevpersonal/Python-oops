# Instance variables inside init


class Computer:
    def __init__(self):
        self.name = 'David'
        self.age = 25


c1 = Computer()
c2 = Computer()
c2.age = 15


# print(c1.name, c1.age)
# print(c2.name, c2.age)


# class variables - static variables


class Car:
    wheels = 4

    def __init__(self):
        self.mileage = 10
        self.color = 'red'


car1 = Car()
car2 = Car()

Car.wheels = 5

print(car1.color, car1.mileage, car1.wheels)
print(car2.color, car2.mileage, car2.wheels)
