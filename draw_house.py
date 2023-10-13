from turtle import *


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
    for x in range(0,4):
        forward(a/5)
        right(90)
    penup()
    left(180)
    forward(-a/3)
    left(90)
    pendown()
    for x in range(0,4):
        forward(a/5)
        right(90)
        


a=200
color("blue")
shape("turtle")
speed(10)
pensize(4)
house(a)

input("...")
