# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:21:08 2020

@author: harsh
"""

######################       GAME DEV WITH TURTLE - PONG [COMPLETE]       #########################

import turtle

window = turtle.Screen()
window.title("Learning PONG")
window.bgcolor("black")
window.setup(width = 640, height = 480)
window.tracer(0)

# Functions to move paddle a
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
    
def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)
    
# Functions to move paddle b
def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)
    
def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)
    
# Keyboard binding
window.listen()
window.onkeypress(pad_a_up, "w")
window.onkeypress(pad_a_down, "s")
window.onkeypress(pad_b_up, "Up")
window.onkeypress(pad_b_down, "Down")

# Score
score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid = 3.5, stretch_len = 0.8)
pad_a.penup()
pad_a.goto(-280, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid = 3.5, stretch_len = 0.8)
pad_b.penup()
pad_b.goto(280, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 180)
pen.write("Player A: 0        Player B: 0", align = "center", font = ("Courier", 18, "bold"))

# Main game loop
while 1:
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border check
    if ball.ycor() > 230:
        ball.sety(230)
        ball.dy *= -1
        
    if ball.ycor() < -230:
        ball.sety(-230)
        ball.dy *= -1
        
    if ball.xcor() > 310:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 18, "bold"))
        
    if ball.xcor() < -310:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 18, "bold"))
        
    # paddle ball collision
    if ball.xcor() > 270 and ball.xcor() < 280 and (ball.ycor() < pad_b.ycor() + 45 and ball.ycor() > pad_b.ycor() - 45):
        ball.setx(270)
        ball.dx *= -1
        
    if ball.xcor() < -270 and ball.xcor() > -280 and (ball.ycor() < pad_a.ycor() + 45 and ball.ycor() > pad_a.ycor() - 45):
        ball.setx(-270)
        ball.dx *= -1
