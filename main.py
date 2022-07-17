import turtle as t
import math

temp = input ("1번째 점의 x좌표를 입력해주세요. : ")
FirstDot = [int(temp)]
temp = input ("1번째 점의 y좌표를 입력해주세요. : ")
FirstDot.append(int(temp))

print("\n")

temp = input ("2째 점의 x좌표를 입력해주세요. : ")
SecondDot = [int(temp)]
temp = input ("2번째 점의 y좌표를 입력해주세요. : ")
SecondDot.append(int(temp))

XChange = FirstDot[0] - SecondDot[0]
YChange = FirstDot[1] - SecondDot[1]

if FirstDot[0] - SecondDot[0] == 0:
    print("잘못된 함수식입니다.")
    exit() 

Slope = YChange / XChange

a = float(Slope)
x = FirstDot[0]
y = FirstDot[1]

b = y - a * x


if a == 1.0:
    print("\n\n일차 함수 식은 y = x + {0:.1f} 입니다. ".format(b))
elif a == 1.0 and b == 1.0:
    print("\n\n일차 함수 식은 y = x 입니다. ")
elif a == 0:
    print("\n\n일차 함수 식은 y = {0:.1f} 입니다. ".format(b))
elif a == -0:
    print("\n\n일차 함수 식은 y = {0:.1f} 입니다. ".format(b))    
elif b == 0:
    print("\n\n일차 함수 식은 y = {0:.1f}x 입니다. ".format(a))
elif b == -0:
    print("\n\n일차 함수 식은 y = {0:.1f}x 입니다. ".format(a))
else:
    print("\n\n일차 함수 식은 y = {0:.1f}x + {1:.1f} 입니다. ".format(a, b))

t.setup(1000, 1000)
t.bgcolor("white")
t.speed(0)

t.goto(0, 0)

t.write("(0, 0)", False, "center", ("", 10))

t.goto(0, -5)
t.fillcolor("black")
t.begin_fill()

t.circle(5)

t.end_fill()

TurtleTemp = 0
t.goto(0, 0)

for x in range(10):
    t.fd(50)
    TurtleTemp = TurtleTemp + 50
    t.write(TurtleTemp, False, "center", ("", 10))

TurtleTemp = 0
t.goto(0, 0)

for x in range(10):
    t.fd(-50)
    TurtleTemp = TurtleTemp - 50
    t.write(TurtleTemp, False, "center", ("", 10))

TurtleTemp = 0
t.goto(0, 0)
t.lt(90)

for x in range(10):
    t.fd(50)
    TurtleTemp = TurtleTemp + 50
    t.write(TurtleTemp, False, "center", ("", 10))

TurtleTemp = 0
t.goto(0, 0)
t.lt(180)

for x in range(10):
    t.fd(50)
    TurtleTemp = TurtleTemp - 50
    t.write(TurtleTemp, False, "center", ("", 10))

TurtleTemp = 0
t.goto(0, 0)
t.lt(90)



# 1번째 점으로 이동

t.penup()
t.goto(FirstDot[0], FirstDot[1])
t.write("{0}, {1}".format(FirstDot[0], FirstDot[1]))

t.goto(FirstDot[0], FirstDot[1] - 5)
t.fillcolor("blue")
t.begin_fill()

t.circle(5)

t.end_fill()

t.goto(FirstDot[0], FirstDot[1])

angle = t.towards(SecondDot[0], SecondDot[1])



# 2번째 점으로 이동

t.goto(SecondDot[0], SecondDot[1])
t.write("{0}, {1}".format(SecondDot[0], SecondDot[1]))

t.goto(SecondDot[0], SecondDot[1] - 5)
t.fillcolor("blue")
t.begin_fill()

t.circle(5)

t.end_fill()

t.goto(FirstDot[0], FirstDot[1])

t.setheading(angle)

t.pendown()
t.pensize(3)
t.fd(5000)
t.fd(-10000)

t.penup()
t.goto(0, 0)
t.hideturtle()


t.done()