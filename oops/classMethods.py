# Instance methods

class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def AverageMarks(self):
        return (self.m1+self.m2+self.m3)/3

s1 = Student(10,10,10)
s2 = Student(20,20,20)

print(s1.AverageMarks())
print(s2.AverageMarks())