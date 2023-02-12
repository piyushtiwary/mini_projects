from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounceY(self):
        self.y_move *= -1

    def bounceX(self):
        self.x_move *= -1

    def reset(self):
        self.goto((0, 0))
        self.bounceX()
