import random

class TurtleGTX():
    def __init__(self):
        self.odometer = 0


    def show_odometer(self):
        return self.odometer

    def forward(self, forward):
        x=random.uniform(0,1)
        y = 0
        if y==1:
            print("you have a flat tyre, can't move")
        else:
            if self.odometer == 0:
                self.odometer += abs(forward)
                #print("1",0.9-(self.odometer**(1/50)-1),x)
            elif x >= (0.9-(self.odometer**(1/50)-1)):
                print("2:",0.9 - (self.odometer ** (1 / 50)-1),"<", x)
                y=1
                #print("flat tyre after:", self.odometer, "meters")
            else:
                self.odometer += abs(forward)
                #print("3", 0.9 - (self.odometer ** (1 / 50) - 1),x)

turtle = TurtleGTX()

turtle.forward(-60)
turtle.forward(300)
turtle.forward(50)

print(turtle.show_odometer())
