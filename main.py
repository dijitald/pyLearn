
import turtle
from time import sleep
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

scr = turtle.Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)

score = Scoreboard()
paddleLeft = Paddle((-350, 0))
paddleRight = Paddle((350, 0))
ball = Ball()

scr.listen()
scr.onkey(paddleLeft.moveUp, "w")
scr.onkey(paddleLeft.moveDown, "s")
scr.onkey(paddleRight.moveUp, "Up")
scr.onkey(paddleRight.moveDown, "Down")

gameOn = True
while gameOn:
    sleep(0.1)
    scr.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    
    if ball.distance(paddleLeft) < 50 and ball.xcor() < -320 or ball.distance(paddleRight) < 50 and ball.xcor() > 320:
        ball.bounceX()
    if ball.xcor() < -380:
        score.updateScore("right")
        ball.reset_position()
    if ball.xcor() > 380:
        score.updateScore("left")
        ball.reset_position()

    if score.scoreLeft == 5 or score.scoreRight == 5: 
        score.declareWinner()
        gameOn = False

scr.exitonclick()


