from turtle import Screen
from sticks import Sticks
from ball import Ball
from score import Score
import time

game_screen = Screen()
game_screen.setup(1000, 700)
game_screen.bgcolor("pink")
game_screen.listen()
gameOn = True
game_screen.tracer(0)

PlayerA = Sticks(-480, 0)
PlayerB = Sticks(480, 0)

pointA = 0
pointB = 0

scoreA = Score(-240, 330)
scoreB = Score(240, 330)

game_screen.onkeypress(PlayerA.leftUp, "w")
game_screen.onkeypress(PlayerA.leftDown, "s")

game_screen.onkeypress(PlayerB.leftUp, "Up")
game_screen.onkeypress(PlayerB.leftDown, "Down")

ball = Ball()

while gameOn:
    game_screen.update()
    time.sleep(0.03)
    ball.move()
    if ball.ycor() > 330 or ball.ycor() < - 330:
        ball.bounceY()

    if ball.distance(PlayerB) < 60 and ball.xcor() > 460 or ball.distance(PlayerA) < 60 and ball.xcor() < -450:
        ball.bounceX()

    if ball.xcor() > 490:
        pointA += 1
        scoreA.update(pointA)
        ball.reset()

    if ball.xcor() < -490:
        pointB += 1
        scoreB.update(pointB)
        ball.reset()


game_screen.exitonclick()
