from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.turtleList = []
        self.create_snake()
        self.head = self.turtleList[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_snake(positions)

    def add_snake(self, position):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.turtleList.append(tim)

    def extend(self):
        self.add_snake(self.turtleList[-1].position())

    def move(self):
        for i in range(len(self.turtleList) - 1, 0, -1):
            new_x = self.turtleList[i - 1].xcor()
            new_y = self.turtleList[i - 1].ycor()
            self.turtleList[i].goto(new_x, new_y)
        self.turtleList[0].fd(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
