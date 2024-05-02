from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

        self.scoreLeft = 0
        self.scoreRight = 0
        self.writeScore()

    def updateScore(self, player):
        if player == "left":
            self.scoreLeft += 1
        else:
            self.scoreRight += 1
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(f"{self.scoreLeft}  {self.scoreRight}", align="center", font=("Courier", 24, "normal"))

    def declareWinner(self):
        if self.scoreLeft > self.scoreRight:
            self.goto(0, 0)
            self.write("Left wins!", align="center", font=("Courier", 36, "normal"))
        else:
            self.goto(0, 0)
            self.write("Right wins!", align="center", font=("Courier", 36, "normal"))



