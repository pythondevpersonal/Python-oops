# Duck typing
class laptop:
    def execute(self,ide):
        ide.execute()


class Pycharm:
    def execute(self):
        print("this is from pyCharm")

ide = Pycharm()
l1 = laptop()
l1.execute(ide)


