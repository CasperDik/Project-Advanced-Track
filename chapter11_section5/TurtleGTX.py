import random
import math

def flat_tyre():
    return random.uniform(0,1)

class TurtleGTX():
    def __init__(self):
        self.odometer = 0
        #self.flat = flat_tyre()

    def show_odometer(self):
        return self.odometer

    def forward(self, forward):
        x=random.uniform(0,1)
        if self.odometer == 0:
            self.odometer += abs(forward)
            print("1",0.9-(self.odometer**(1/50)-1),x)
        if x >= (0.9-(self.odometer**(1/50)-1)):
            print("2",0.9 - (self.odometer ** (1 / 50)-1),x)
            print("flat tyre after:", self.odometer, "meters")
        else:
            self.odometer += abs(forward)
            print("3", 0.9 - (self.odometer ** (1 / 50) - 1),x)

turtle = TurtleGTX()
turtle.forward(50)
turtle.forward(-60)
turtle.forward(300)

print(turtle.show_odometer())
