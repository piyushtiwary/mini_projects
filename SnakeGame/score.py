from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.hideturtle()
        self.goto(x=0, y=280)
        self.color("white")
        self.write(f"Score: {self.my_score}", align="center")

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.my_score += 1
        self.clear()
        self.write(f"Score: {self.my_score}", align="center")
