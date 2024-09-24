import turtle

t= turtle.Turtle()

turtle.bgcolor('black')
# t.pencolor('green')

colors = ['red', 'green','orange', 'blue']
t.speed(0)
for x in range(100):
    t.pencolor(colors[x%4])
    # t.forward(2*x) #use either of forward or circle
    t.circle(x)
    t.left(91)


turtle.mainloop()