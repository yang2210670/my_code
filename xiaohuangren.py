import turtle as t
t.hideturtle()
t.penup()
t.goto(0,200)
t.speed(20)
t.pensize(3)
t.pendown()
t.colormode(255)
t.fillcolor((255,230,0))
t.begin_fill()
for i in range(5):
    t.right(1)
    t.fd(6)
t.circle(-80,80)
t.fd(20)
t.seth(-90)
t.fd(200)
t.seth(180)
t.penup()
t.fd(217.5)
t.pendown()
t.seth(90)
t.fd(202)
t.seth(80)
t.fd(24)
t.circle(-80,80)
for i in range(5):
    t.left(1)
    t.fd(6)
t.end_fill()
#
t.fillcolor("black")
t.begin_fill()
t.pensize(1)
t.seth(40)
for i in range(5):
    t.right(6)
    t.fd(20)
t.seth(160)
for i in range(5):
    t.left(1)
    t.fd(4)
t.seth(180)
t.fd(2)
for i in range(4):
    t.left(9)
    t.fd(12)
for i in range(4):
    t.left(1)
    t.fd(10)
t.seth(180)
t.fd(5)
t.seth(130)
for i in range(7):
    t.left(5)
    t.fd(10)
for i in range(4):
    t.left(9)
    t.fd(10)
t.seth(10)
for i in range(4):
    t.right(11)
    t.fd(25)
t.end_fill()
#画左眼
t.fillcolor("black")
t.begin_fill()
t.penup()
t.goto(-110,134)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.pensize(1)
t.seth(-20)
t.fd(40)
t.seth(70)
t.circle(-35,345)
t.seth(163)
t.fd(40)
t.end_fill()
#
t.penup()
t.goto(-30,139)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.circle(32)
t.end_fill()
#
t.penup()
t.goto(-34,125)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.circle(17)
t.end_fill()
#
t.penup()
t.goto(-33,121)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.circle(10)
t.end_fill()
#画右眼
t.fillcolor("black")
t.begin_fill()
t.penup()
t.goto(103,134)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.pensize(1)
t.seth(200)
t.fd(40)
t.seth(110)
t.circle(35,345)
t.seth(17)
t.fd(37)
t.end_fill()
#
t.penup()
t.goto(23,139)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.circle(-32)
t.end_fill()
#
t.penup()
t.goto(27,125)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.circle(-17)
t.end_fill()
#
#
t.penup()
t.goto(33,121)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.circle(-10)
t.end_fill()
#画嘴巴
t.pensize(2)
t.penup()
t.goto(-32,10)
t.fillcolor("white")
t.begin_fill()
t.pendown()
t.seth(15)
t.fd(70)
t.seth(-115)
for i in range(4):
    t.right(3)
    t.fd(7)
for i in range(8):
    t.right(10)
    t.fd(5)
for i in range(6):
    t.right(6)
    t.fd(3)
t.end_fill()
#画裤子
t.pensize(3)
t.penup()
t.goto(-114,-90)
t.fillcolor((70,130,200))
t.begin_fill()
t.seth(-90)
t.pendown()
t.circle(109,180)
t.seth(180)
t.fd(20)
t.right(90)
t.fd(50)
t.left(90)
t.fd(177)
t.left(90)
t.fd(50)
t.seth(180)
t.fd(20)
t.end_fill()
#
t.pensize(3)
t.penup()
t.goto(-112,-10)
t.fillcolor((70,130,200))
t.begin_fill()
t.pendown()
t.seth(-40)
t.fd(70)
t.seth(-130)
t.fd(20)
t.seth(140)
t.fd(55)
t.end_fill()
t.penup()
t.goto(-72,-52)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.circle(2)
#
t.pensize(3)
t.penup()
t.goto(102,-10)
t.fillcolor((70,130,200))
t.begin_fill()
t.pendown()
t.seth(-140)
t.fd(70)
t.seth(-50)
t.fd(20)
t.seth(40)
t.fd(55)
t.end_fill()
t.penup()
t.goto(65,-55)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.circle(2)
t.end_fill()
#裤子细节
t.penup()
t.goto(-30,-100)
t.pendown()
t.seth(0)
t.fd(60)
t.seth(-90)
t.circle(-30,180)
t.penup()
t.goto(0,-197)
t.pendown()
t.seth(90)
t.fd(40)
t.penup()
t.goto(-107,-130)
t.pendown()
t.seth(0)
for i in range(5):
    t.left(15)
    t.fd(7)
t.penup()
t.goto(97,-130)
t.pendown()
t.seth(180)
for i in range(5):
    t.right(15)
    t.fd(7)    
#画左手
t.penup()
t.goto(-114,-35)
t.fillcolor((255,230,0))
t.begin_fill()
t.pendown()
t.seth(-135)
t.fd(40)
t.seth(-90)
t.fd(5)
t.seth(-40)
t.fd(36)
t.end_fill()
t.penup()
t.goto(-114,-60)
t.seth(-135)
t.pendown()
t.pensize(5)
t.fd(4)
#画右手
t.pensize(3)
t.penup()
t.goto(105,-35)
t.fillcolor((255,230,0))
t.begin_fill()
t.pendown()
t.seth(-45)
t.fd(40)
t.seth(-90)
t.fd(5)
t.seth(-140)
t.fd(36)
t.end_fill()
t.penup()
t.goto(105,-60)
t.seth(-45)
t.pendown()
t.pensize(5)
t.fd(4)
#画左脚
t.penup()
t.pensize(3)
t.goto(-30,-195)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.seth(-90)
t.fd(20)
t.seth(110)
for i in range(7):
    t.left(20)
    t.fd(7)
t.seth(-90)
t.fd(5)
t.seth(-70)
for i in range(3):
    t.left(15)
    t.fd(5)
for i in range(5):
    t.left(2)
    t.fd(1)
t.seth(0)
t.fd(45)
t.seth(90)
t.fd(40)
t.end_fill()
#画右脚
t.penup()
t.pensize(3)
t.goto(30,-195)
t.fillcolor("black")
t.begin_fill()
t.pendown()
t.seth(-90)
t.fd(20)
t.seth(70)
for i in range(7):
    t.right(20)
    t.fd(7)
t.seth(-90)
t.fd(5)
t.seth(-110)
for i in range(3):
    t.right(15)
    t.fd(5)
for i in range(5):
    t.right(2)
    t.fd(1)
t.seth(180)
t.fd(45)
t.seth(90)
t.fd(40)
t.end_fill()





















































