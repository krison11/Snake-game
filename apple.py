
from turtle import Turtle
import random

# inheriting everything from the Turtle Class and using its methods without defining new attributes


class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('red')
        self.up()
        self.speed('fastest')
        self.change_position()

    def change_position(self):
        pos_x = random.randint(-220, 220)
        pos_y = random.randint(-220, 220)
        self.goto(x=pos_x, y=pos_y)
