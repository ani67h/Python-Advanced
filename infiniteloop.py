import turtle #importing turtle
loadWindow = turtle.Screen()
turtle.speed(1000000) #speed of turtle

for i in range(10000000): #iterate for loop
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()    