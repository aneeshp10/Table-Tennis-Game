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
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

playerOne = 0
playerTwo = 0

score = turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,255)
score.write("Player 1: 0                                            Player 2: 0", align="center", font=("Georgia", 24, "bold"))

winner = turtle.Turtle()
winner.hideturtle()
winner.penup()
winner.goto(0,-50)
winner.color("white")

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
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        playerOne+=1
        score.clear()
        if (playerOne == 7) :
            winner.write("Player One Wins", align="center", font=("Georgia", 24, "normal"))
            ball.color("blue")
            ball.dx = 0
            ball.dy = 0
        
        score.write("Player 1: {}                                            Player 2: {}".format(playerOne, playerTwo), align="center", font=("Georgia", 24, "bold"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    if ball.xcor() < -390:
        playerTwo+=1
        score.clear()
        if (playerTwo == 7) :
            winner.write("Player Two Wins", align="center", font=("Georgia", 24, "normal"))
            ball.color("blue")
            ball.dx = 0
            ball.dy = 0

        score.write("Player 1: {}                                            Player 2: {}".format(playerOne, playerTwo), align="center", font=("Georgia", 24, "bold"))
        
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    # Collisions
    if (ball.xcor() > 340) :
        if (ball.xcor() < 350) :
            if (paddleTwo.ycor() - 40 < ball.ycor() < paddleTwo.ycor() + 40) :
                ball.setx(340)
                ball.dx = ball.dx * - 1

    if (ball.xcor() < -340) :
        if (ball.xcor() > -350) :
            if (paddleOne.ycor() - 40 < ball.ycor() < paddleOne.ycor() + 40) :
                ball.setx(-340)
                ball.dx = ball.dx * - 1