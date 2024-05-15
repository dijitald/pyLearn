import turtle

class Paddle (turtle.Turtle):
    def __init__(self, startPos):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(startPos)

    def moveUp(self):
        if (self.ycor() < self.screen.window_height()/2):
            self.sety(self.ycor() + 20)

    def moveDown(self):
        if (self.ycor() > -self.screen.window_height()/2):
            self.sety(self.ycor() - 20)
