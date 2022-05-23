import turtle

window = turtle.Screen()
window.bgcolor("black") 

brad = turtle.Turtle()
brad.shape("arrow")
brad.pensize(5)
brad.color("white")

for i in range(8):    
    brad.forward(80)
    brad.left(45)

window.exitonclick()