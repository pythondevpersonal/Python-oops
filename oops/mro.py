# Method Resolution Order - left to right

class A:
    def __init__(self):
        print("A init")

    def feature1(self):
        print("Feature 1-A")

class B:
    def __init__(self):
        print("B init")

    def feature1(self):
        print("Featue 1-B")

    def feature2(self):
        print("Featue 2-B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")

    def feature1(self):
        print("Featue 1-C")

    def feature2(self):
        print("Featue 2-C")


c1 = B()
c1.feature1()