import turtle #importing turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #defined variable
polygon.speed(1)
              
num_sides = 6 #variable
side_length = 70
angle = 360 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()