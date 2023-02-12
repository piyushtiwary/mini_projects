from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self. penup()
        self.hideturtle()
        self.move()

    def move(self):
        self.goto(self.x, self.y)

    def displayScore(self, point):
        self.write(point, font=("Arial", 12, "normal"))

    def update(self, point):
        self.clear()
        self.displayScore(point)

