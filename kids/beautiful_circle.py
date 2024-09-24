import turtle

t= turtle.Turtle()

turtle.bgcolor('black')
# t.pencolor('green')

colors = ['red', 'green','orange', 'blue','purple','brown']

t.speed(0)
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(60)


turtle.mainloop()