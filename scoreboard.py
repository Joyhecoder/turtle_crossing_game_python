from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        

    def update_scoreboard(self):
        self.goto(0, 0)
        self.level += 1
        self.write(f"You are on level {self.level}", align="center", font=FONT)
    
    def clear_scoreboard(self):
        self.write("", align="center", font=FONT)
        
        
