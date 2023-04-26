from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        self.forward(10)

    def gameOver(self):
        self.goto(0, 0)
        self.write("You Win", align="center", font=("Arial", 24, "normal"))
