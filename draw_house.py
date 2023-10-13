from turtle import *
import random


def square(a):
    for x in range(0,4):
        forward(a)
        right(90)

def square2(a):
    i = 0       
    while i < 4:
        forward(a)
        right(90)
        i = i + 1

def triangle(a):
    for i in range(0,3):
        forward(a)
        left(120)


def house(a):
    x=-a/2
    y=a/2
    penup()
    goto(x,y)
    pendown()
    # ve than nha
    square2(a)
    # ve mai nha
    triangle(a)
    # ve cua so ben trai
    penup()
    forward(a/3)
    right(90)
    forward(a/3)
    right(90)
    pendown() 
    square2(a/4)

    penup()
    left(180)
    forward(a/3)
    left(90)
    pendown()
    square2(a/4)
        
def rectangle(a):
    penup()
    x=0
    y=-23
    goto(x,y)
    right(90)
    forward(5)
    pendown()
    for x in range(0,4):
        forward(a/13)
        right(90)
        forward(a/5)


a=100
color("blue")
shape("turtle")
speed(10)
pensize(4)
house(a)
rectangle(a)
colours = ["white","cyan","yellow","orange","purple","pink","red","green"]
pensize(6)
shape("turtle")
speed(200)
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
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)




input("...")
