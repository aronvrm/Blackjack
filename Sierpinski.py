import turtle

t = turtle.Turtle()

t.right(270)
t.pu()
t.ht()

window = turtle.Screen()


t.speed(200)
t.pen(fillcolor="black", pencolor="black", pensize=1)
t.color('red')


def sierpinski(size, order):
    if order == 0:
        t.stamp()
    else:
        for i in range(0, 3):
            t.forward(size)
            sierpinski(size/2, order-1)
            t.backward(size)
            t.left(120)


sierpinski(200, 6)

window.exitonclick()
