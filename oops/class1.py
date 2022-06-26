class Computer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return "Name:" + self.name + ', Age: ' + str(self.age)

    def compare(self,other):
        if self.age == other.age:
            return True
        return False


obj1 = Computer("David",25)
obj2 = Computer("Murugan", 26)
obj2.age = 25
# print(obj1.compare(obj2))


class Human:
    def __init__(self):
        self.name = "Ashok"
        self.age = 25

    def display(self):
        return "Name:" + self.name + ', Age: ' + str(self.age)

    def compare(self,other):
        if self.age == other.age:
            return True
        return False

human1 = Human()
human1.age=25
human2 = Human()

# print(human1.compare(human2))
