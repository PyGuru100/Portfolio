from turtle import Screen
from classes_and_constants import Ball, Paddle, Enemies, GAME_WIDTH, GAME_HEIGHT, CollisionDetector

# initialize screen:
screen = Screen()
screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
screen.tracer(0)
# initialize game objects:
paddle = Paddle()
enemies = Enemies()
ball = Ball(x_motion=3.5)
collision_detector = CollisionDetector(ball=ball, enemies=enemies, paddle=paddle)

# define controls:
MOVEMENT_CONSTANT = 50


def left():
    if paddle.xcor() <= (-GAME_WIDTH/2 + MOVEMENT_CONSTANT):
        return
    paddle.goto(paddle.xcor() - MOVEMENT_CONSTANT, paddle.ycor())


def right():
    if paddle.xcor() >= (GAME_WIDTH/2 - MOVEMENT_CONSTANT):
        return
    paddle.goto(paddle.xcor() + MOVEMENT_CONSTANT, paddle.ycor())


screen.listen()
screen.onkeyrelease(key='a', fun=left)
screen.onkeyrelease(key='d', fun=right)


while True:
    ball.move()
    collision_detector.collision_detection()
    if not paddle.alive:
        break
    screen.update()
screen.exitonclick()
