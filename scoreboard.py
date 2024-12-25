from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):   
        self.clear()         
        self.goto(-100,200)
        self.write(self.lscore, align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(self.rscore, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.lscore+=1
        self.update_scoreboard()

    def r_point(self):
        self.rscore+=1
        self.update_scoreboard()
