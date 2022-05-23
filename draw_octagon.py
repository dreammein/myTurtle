import turtle

window = turtle.Screen()
window.bgcolor("black") 

brad = turtle.Turtle()
brad.pensize(5)
brad.shape("arrow")
brad.color("white")
brad.fillcolor('red')

brad.begin_fill()
for i in range(8):    
    brad.forward(80)
    brad.left(45)
brad.end_fill() 

brad.hideturtle()

window.exitonclick()