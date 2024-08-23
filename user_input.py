# user_input.py

from turtle import *


for i in range(3):
    drawing = input("What would you like me to draw? ")
    size = int(input("How big should I draw it? "))

    if drawing == "square":
        for i in range(4):
            forward(size)
            right(90)
            
    elif drawing == "circle":
        circle(size)

    else:
        print("Sorry, I don't know how to draw that...")

    clear()