# import turtle library
import turtle             
#col = [ "red","purple","blue","green","orange","yellow"]
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(25)
for i in range(150):
    t.color('white')
    t.forward(i*1.2)
    t.right(40)
    t.width(1)