import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    n = 3  # при бажанні можна погратися з кількістю граней у фігурі
    for _ in range(n):
        koch_curve(t, order, size)
        t.right(360 / n)

    window.mainloop()


# Виклик функції
draw_koch_curve(3)
