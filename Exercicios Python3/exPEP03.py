import turtle
import math

bob = turtle.Turtle()


def Quadrado(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def poligono(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def Circulo(t, r):
    ciref = 2 * math.pi * r
    n = 50
    length = ciref / n
    poligono(t, n, length)


Circulo(bob, 50)

turtle.mainloop()
