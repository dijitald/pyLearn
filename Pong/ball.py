
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0.5)
        self.stepX = 10
        self.stepY = 10
        self.moveSpeed = 0.1

    def move(self):
        self.setx(self.xcor() + self.stepX)
        self.sety(self.ycor() + self.stepY)

    def bounceY(self):
        self.stepY *= -1

    def bounceX(self):
        self.stepX *= -1
        self.moveSpeed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.bounceX()
