from turtle import Turtle

class Sticks(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.penup()
        self.shape("square")
        self.shapesize(6, 0.5, 10)
        self.color("brown")
        self.set_location()

    def set_location(self):
        self.goto(self.x, self.y)

    def leftUp(self):
        self.sety(self.ycor()+10)

    def leftDown(self):
        self.sety(self.ycor()-10)



