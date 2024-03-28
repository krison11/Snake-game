from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
SNAKE_MOVE_DISTANCE = 11
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        s = Turtle()
        s.color('white')
        s.shape('square')
        s.shapesize(0.5)
        s.up()
        s.goto(pos)
        self.segments.append(s)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_pos = self.segments[i-1].pos()
            self.segments[i].goto(new_pos)
        self.head.fd(SNAKE_MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
