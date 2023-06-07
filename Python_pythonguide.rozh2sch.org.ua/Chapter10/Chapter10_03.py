class Printer():
    def __init__(self):
        pass

    def does(self):
        return('print')

class Lamp():
    def __init__(self):
        pass

    def does(self):
        return('glow')

class Car():
    def __init__(self):
        pass

    def does(self):
        return('ride')


class Robot():
    def __init__(self):
        self.printer = Printer()
        self.lamp = Lamp()
        self.car = Car()

    def do_it(self):
        print(self.printer.does(), self.lamp.does(), self.car.does())


robot = Robot()
robot.do_it()