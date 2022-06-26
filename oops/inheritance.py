# Multiple inheritance

class A:
    def feature1(self):
        print('Feature 1')

class B:
    def feature2(self):
        print('Feature 2')

class C(A,B):
    def feature3(self):
        print('Feature 3')

c3 = C()
c3.feature1()