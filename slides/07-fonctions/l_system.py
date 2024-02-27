from turtle import *

def draw(seq, length):
    for action in seq:
        match action.lower():
            case "f":
                forward(length)
            case "+":
                left(90)
            case "-":
                right(90)


