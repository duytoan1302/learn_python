from turtle import *
import random
shape("turtle")
speed(10)
colours = ["white","cyan","yellow","orange","purple","pink","red","green"]
pensize(6)
Screen().bgcolor("turquoise")
def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)

def snowflakeArm(size):
    for x in range (0,4):
        forward(size)
        vshape(size)
    backward(size*4)

def snowflake(size):
    for x in range(0,18):
        color(random.choice(colours))
        snowflakeArm(size)
        right(20)
for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)
