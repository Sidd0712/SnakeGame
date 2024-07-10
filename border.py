from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.goto(300, 300)
        self.pendown()
        pos = 180
        for _ in range(4):
            self.setheading(pos)
            self.forward(600)
            pos += 90
