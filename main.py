from turtle import Screen
import time
from snake import Snake
from apple import Apple
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)


snake = Snake()
apple = Apple()
score_board = ScoreBoard()


screen.listen()

screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Up', fun=snake.turn_up)
screen.onkey(key='Down', fun=snake.turn_down)


def snake_touches_tail():
    for s in snake.segments:
        if s == snake.head:
            pass
        elif snake.head.distance(s) < 10:
            return True
        else:
            return False


play = True
message = ''

while play:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if snake eats apple
    if snake.head.distance(apple) < 10:
        score_board.increase_score()
        snake.extend()
        apple.change_position()
    # if snake hits the wall
    if snake.segments[0].xcor() > 250 or snake.segments[0].xcor() < -250 or snake.segments[0].ycor() > 250 or snake.segments[0].ycor() < -250:
        score_board.message = 'You hit the wall.'
        score_board.game_over()
        play = False
    # if snake hits tail except the head
    for s in snake.segments[2:]:
        if snake.head.distance(s) < 10:
            score_board.message = 'You hit your tail.'
            score_board.game_over()
            play = False


screen.exitonclick()
