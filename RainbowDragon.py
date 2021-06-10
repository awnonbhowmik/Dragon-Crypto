import turtle

ob=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
ob.speed('fastest')
ob.hideturtle()

ob.goto(0,0)
wn.tracer(n=10,delay=None)

colors = ["violet","indigo","blue","light green","yellow","orange","red"]

def dragoncurve(ob,l,n):
  for i in range(1):
    def x(n):
            if n==0:
                    return
            x(n-1)
            ob.right(90)
            y(n-1)
            ob.forward(l)
    def y(n):
            if n==0:
                    return
            ob.forward(l)
            x(n-1)
            ob.left(90)
            y(n-1)
    ob.fd(l)
    x(n)

for i in range(len(colors)):
  ob.pencolor(colors[i])
  ob.setheading(360/7*i)
  dragoncurve(ob,2,12)
  print(ob.pos())
  ob.penup()
  ob.goto(0,0)
  ob.pendown()
