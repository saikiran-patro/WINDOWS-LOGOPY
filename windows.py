# WINDOWS-LOGOPY
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
def smsquare(length,angle):
    t.forward(length)
    t.right(angle)


t.color("deepskyblue")
t.left(6)
t.begin_fill()
t.fillcolor("deepskyblue")
smsquare(200,96)
smsquare(150,96)
smsquare(200,83)
smsquare(109,85)
t.end_fill()
t.color("black")
smsquare(100,96)
smsquare(67,90)
smsquare(100,180)
smsquare(200,180)
smsquare(100,270)
t.forward(140)
turtle.exitonclick()
