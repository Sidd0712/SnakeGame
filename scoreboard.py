from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def save_highscore(self):
        with open("high_score_saver.txt", mode="w") as high_score_file:
            high_score_file.write(str(self.high_score))

    def get_high_score(self):
        with open("high_score_saver.txt", mode="r") as high_score_file:
            return int(high_score_file.read())

