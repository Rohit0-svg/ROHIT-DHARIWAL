import turtle
t = turtle.Turtle()
t.screen.bgcolor("black")
t.speed(0)
t.pensize(1)

colors = ["pink", "hotpink", "deeppink", "palevioletred"]

for x in range(150):
    t.color(colors[x % 4])
    t.circle(x)
    t.left(30)

t.hideturtle()
turtle.done()



# fibbonacci series with the help of for loop
a=0     # 0 1 1 2 3 5 8 13
b=1
print(a)
print(b)
for i in range(6) :
    c = a + b
    print(c)
    a = b
    b = c
print ("done ")