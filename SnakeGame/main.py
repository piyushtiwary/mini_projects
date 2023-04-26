from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Score

game_screen = Screen()
game_screen.setup(height=600, width=600)
game_screen.title("Snake Game")
game_screen.tracer(0)
game_screen.bgcolor("black")

gameOn = True

my_snake = Snake()
food = Food()
game_screen.listen()
score = Score()

game_screen.onkey(my_snake.up, "w")
game_screen.onkey(my_snake.down, "s")
game_screen.onkey(my_snake.left, "a")
game_screen.onkey(my_snake.right, "d")


while gameOn:
    game_screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 17:
        food.refresh()
        my_snake.extend()
        score.increase_score()

    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        gameOn = False
        score.gameOver()

    for snake in my_snake.turtleList[1:]:
        if my_snake.head.distance(snake) < 10:
            score.gameOver()
            gameOn = False


game_screen.exitonclick()
