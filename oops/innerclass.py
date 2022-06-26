class Student:
    def __init__(self):
        self.name = 'Murugan'
        self.age = 25
        self.address = "hello"
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.cpu = '2'
            self.brand = "HP"

        def show(self):
            print(self.brand, self.cpu)

s1 = Student()
s1.show()

print(s1.lap.brand)