#imports

import turtle
import time

wn = turtle.Screen()
wn.title("Dong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.speedx = 2
ball.speedy = 2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Score
a_score = 0
b_score = 0

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 235:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -225:    
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 235:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -225:    
        y -= 20
        paddle_b.sety(y)

def newgame():
    a_score = 0
    b_score = 0
    paddle_a.goto(-350,0)
    paddle_b.goto(350,0)
    pen.goto(0, 260)
    pen.clear()
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Keyboard Binds
wn.listen()

#Paddle A
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

#Paddle B
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop

while True:
   wn.update()
   time.sleep(1/120)

   #Check for win
   if int(a_score) == 10 or (b_score) == 10:
       pen.clear()
       pen.goto(0, 200)
       if a_score > b_score:
           pen.write("GAME OVER PLAYER A WINS!!", align="center", font= ("Courier", 35, "normal"))
           time.sleep(10)
           newgame()
       if b_score > a_score:
           pen.write("GAME OVER PLAYER B WINS!!", align="center", font= ("Courier", 35, "normal"))
           time.sleep(10)
           newgame()        

#Move the ball
   ball.setx(ball.xcor()+ball.speedx)
   ball.sety(ball.ycor()+ball.speedy)

#Border check
   if ball.ycor() > 290:
      ball.sety(290)
      ball.speedy *= -1

   if ball.ycor() < -290:
      ball.sety(-290)
      ball.speedy *= -1
   
   if ball.xcor() > 390:
      a_score += 1
      ball.goto(0,0)
      ball.speedx = 2
      ball.speedy = 2
      ball.speedx *= -1
      pen.clear()
      pen.write("Player A: {}  Player B: {}".format(a_score, b_score), align="center", font=("Courier", 24, "normal"))


   if ball.xcor() < -390:
      b_score += 1
      ball.goto(0,0)
      ball.speedx = 2
      ball.speedy = 2
      ball.speedx *= -1
      pen.clear()
      pen.write("Player A: {}  Player B: {}".format(a_score, b_score), align="center", font=("Courier", 24, "normal"))

#Paddle collision

   if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
       ball.setx(340)
       ball.speedx *=1.1
       ball.speedy *=1.1
       ball.speedx *= -1

   if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
      ball.setx(-340)
      ball.speedx *=1.1
      ball.speedy *=1.1
      ball.speedx *= -1
