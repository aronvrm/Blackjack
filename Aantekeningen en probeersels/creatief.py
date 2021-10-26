from turtle import *
import turtle
import sys
from time import sleep


t = turtle.Turtle()
window = turtle.Screen()
t.speed(0)


# creating turtle pen
t = turtle.Turtle()


def zelf_tekenen():

    n = int(input("Hoeveel kanten moet je figuur bevatten? : "))

    l = int(input("Hoelang moet de kanten van je figuur worden? : "))

    words = "Bedankt, de rest ga ik voor je tekenen, let maar op!"

    for char in words:
        sleep(0.075)
        sys.stdout.write(char)
        sys.stdout.flush()

    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)


zelf_tekenen()


def automatisch_tekenen():
    t.begin_fill()
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.end_fill()


automatisch_tekenen()


def automatisch_tekenen_2():
    t.begin_fill()
    t.fd(10)
    t.lt(12)
    t.fd(10)
    t.lt(12)
    t.fd(10)
    t.end_fill()


automatisch_tekenen_2()


window.exitonclick()
