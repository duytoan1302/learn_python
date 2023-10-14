
from turtle import *

NUM_OF_SQUARES = 10
SQUARE_SIZE = 20
SIZE_INCREMENT = 10  # moi hinh vuong tang kich thuoc them 10


def square(a):
    for x in range(0, 4):
        forward(a)
        right(90)


curSize = SQUARE_SIZE
totalSize = 0
for i in range(0, NUM_OF_SQUARES):
    totalSize = totalSize + curSize
    curSize = curSize + SIZE_INCREMENT

# x0 = -(SQUARE_SIZE*NUM_OF_SQUARES/2 + NUM_OF_SQUARES/2-1)
x0 = -(totalSize/2 + NUM_OF_SQUARES/2-1)
y0 = SQUARE_SIZE/2
penup()
goto(x0, y0)

speed(30)
color("red")
shape("turtle")
pensize(4)

curSize = SQUARE_SIZE
for i in range(0, NUM_OF_SQUARES):
    pendown()
    square(curSize)

    # di chuyen de ve hinh vuong tiep theo ben phai
    penup()
    # ... ++x => di qua phai
    forward(curSize+1)
    # ... ++y => di len tren
    left(90)
    forward(SIZE_INCREMENT/2)
    right(90)

    # tang kich thuoc hinh vuong sau moi lan ve
    curSize = curSize+SIZE_INCREMENT

# dung lai cho xem ket qua
input("...")
