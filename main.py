from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My pong game.")

screen.tracer(0)
screen.listen()

r_player = Player((350, 0))
l_player = Player((-350, 0))

screen.onkey(r_player.up, "i")
screen.onkey(r_player.down, "k")
screen.onkey(l_player.up, "w")
screen.onkey(l_player.down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()



