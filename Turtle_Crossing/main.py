from turtle import Screen
from cars import Car
from player import Player
import time

gameOn = True
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.listen()
game_screen.tracer(0)

player = Player()
cars = Car()

while gameOn:
    game_screen.onkey(player.move_up, "Up")
    game_screen.update()
    time.sleep(0.1)
    cars.create()
    cars.move()

    for car in cars.carList:
        if car.distance(player) < 20:
            gameOn = False

    if player.ycor() > 280:
        Player.gameOver(player)
        gameOn = False

game_screen.exitonclick()
