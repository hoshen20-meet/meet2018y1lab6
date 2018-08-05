import turtle

colors = ['green','blue','orange', 'red']


turtle.speed(900)
for i in range(99999999):
    turtle.pencolor(colors[i%4])
    turtle.bgcolor('black')
    turtle.forward(i)
    turtle.degrees()

    turtle.right(70)
    
    
    

