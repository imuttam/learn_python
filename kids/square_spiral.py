import turtle

t= turtle.Turtle()

turtle.bgcolor('black')
t.pencolor('green')



for x in range(100):
    t.forward(2*x) #use either of forward or circle
    t.circle(x)
    t.left(91)


turtle.mainloop()