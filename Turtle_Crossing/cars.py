from turtle import Turtle
import random


class Car:

    def __init__(self):
        self.carList = []

    def create(self):
        num = random.randint(1, 3)
        if num == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
            car.shapesize(stretch_wid=0.5, stretch_len=1)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.carList.append(car)

    def move(self):
        for cars in self.carList:
            cars.backward(10)
