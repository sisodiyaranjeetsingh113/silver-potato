""" 
import turtle
col = ('red', 'yellow', 'green', 'cyan')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(25)
n = True
while n:
    print('''1 => patern1  
    \n2 => patern2
    \n3 => patern3
    \n4 =>Exit''')
    ch = int(input("Enter your Choice :"))
    if ch == 1:
        screen = turtle.Screen()
        for i in range(0, 4, 1):
            t.color(col[i % 4])
            if i == 0:
                pass
            else:
                t.left(90)
            t.forward(80)
            t.right(90)
            t.forward(80)
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(40)
            t.left(90)
            t.forward(40)
    if ch == 2:
        screen = turtle.Screen()
        t.color('yellow')
        t.left(30)
        t.forward(120)
        t.right(75)
        t.forward(80)
        t.right(105)
        t.forward(120)
        t.right(75)
        t.forward(80)
        t.color('cyan')
        t.left(135)
        t.forward(20)
        t.left(45)
        t.forward(80)
        t.left(75)
        t.forward(120)
        t.left(60)
        t.forward(20)
    if ch == 3:
        screen = turtle.Screen()
        t.forward(115)
        t.left(90)
        t.color('red')
        for i in range(900):
            t.left(.5)
            t.forward(1)
        t.color('white')
        t.forward(115)
        t.left(90)
        t.forward(230)
        t.left(90)
        t.forward(230)
        t.left(90)
        t.forward(230)
        t.left(90)
        t.forward(115)
        t.left(90)

    if ch == 4:
        screen = turtle.Screen()
        t.width(1)
        for i in range(31):
            t.color(col[i % 4])
            if i % 4 == 0:
                t.left(45)
                t.forward(80)
            else:
                pass
            t.right(135)
            t.forward(80)
            t.right(135)
            t.forward(80)
            t.left(135)
            t.forward(80)
"""