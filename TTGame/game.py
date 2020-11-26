import turtle

wn = turtle.Screen()
wn.title("Aneesh P")
wn.bgcolor("blue")
wn.setup(width=800, height= 600)
wn.tracer(0)

# Paddle One
paddleOne = turtle.Turtle()
paddleOne.speed(0)
paddleOne.shape("square")
paddleOne.color("green")
paddleOne.shapesize(stretch_wid=5, stretch_len= 1)
paddleOne.penup()
paddleOne.goto(-350, 0)

# Paddle B
paddleTwo = turtle.Turtle()
paddleTwo.speed(0)
paddleTwo.shape("square")
paddleTwo.color("green")
paddleTwo.shapesize(stretch_wid=5, stretch_len= 1)
paddleTwo.penup()
paddleTwo.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.color("green")

# left bat going up
def paddleOneUp():
    y = paddleOne.ycor()
    y = y + 30
    paddleOne.sety(y)

# left bat going down
def paddleOneDown():
    y = paddleOne.ycor()
    y = y - 30
    paddleOne.sety(y)

def paddleTwoUp():
    y = paddleTwo.ycor()
    y = y + 30
    paddleTwo.sety(y)

def paddleTwoDown():
    y = paddleTwo.ycor()
    y = y - 30
    paddleTwo.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddleOneUp, "w")
wn.onkeypress(paddleOneDown, "s")

wn.onkeypress(paddleTwoUp, "Up")
wn.onkeypress(paddleTwoDown, "Down")


while True:
    wn.update()