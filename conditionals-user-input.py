######################
# Unit 0 Lab 4
# conditionals-user-input.py
#######################

from turtle import *

while True:
    
    drawing = input("What would you like me to draw? ")
    size = int(input("How big should I draw it? "))
    if drawing == "square":
        for i in range(4):
            forward(size)
            right(90)
    elif drawing == "quit":
        break
    else:
        print("Sorry, I don't know how to draw that...")

    clear()