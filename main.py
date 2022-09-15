from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
speed = 0.1



game_is_on = True

while game_is_on:
  time.sleep(speed)
  screen.update()
  ball.move()
  if ball.ycor() > 280 or ball.ycor() < - 280:
    ball.bounce_y()
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
    
    ball.bounce_x()
    speed *= 0.9
  if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    speed *= 0.9
    
    ball.bounce_x()

  if ball.xcor() > 380:
    ball.reset()
    speed = 0.1
    scoreboard.l_point()
    ball.bounce_x()

  if ball.xcor() < -380:
    ball.reset()
    speed = 0.3
    scoreboard.r_point()
    ball.bounce_x()  
      
     




















screen.exitonclick
