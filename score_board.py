from turtle import Turtle
POSITION = (0, 230)
COLOR = 'white'
ALIGNMENT = 'center'
FONT = ('Arial', 15, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.message = ''
        self.hideturtle()
        self.goto(POSITION)
        self.color(COLOR)
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'   GAME OVER\n{self.message}', align=ALIGNMENT, font=FONT)
