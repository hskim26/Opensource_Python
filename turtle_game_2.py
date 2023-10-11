import turtle as t
from random import randint

print("**** 거북이 게임을 시작합니다. ********************")
print("* 거북이 선수를 선택하세요 : ")
name = []

for i in range(4):
    turtle_name = input(f"거북이 {i + 1}번 : ")
    name.append(turtle_name)

# 경기장 그리기
t.speed(10)
t.penup()
t.goto(-140, 140)

for step in range(15):
    t.write(step, align='center')
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(200)
    t.penup()
    t.backward(210)
    t.left(90)
    t.forward(20)
t.hideturtle()

# 게임 플레이어 준비
colors = ['red', 'yellow', 'green', 'blue']
players = [0, 0, 0, 0]

for i in range(len(colors)):
    players[i] = t.Turtle()
    players[i].color(colors[i])
    players[i].shape('turtle')
    players[i].penup()
    players[i].goto(-160, 100 - i * 50)  # 각 거북이를 수직으로 50 픽셀씩 이동
    players[i].pendown()
    players[i].pensize(5)


#게임 시작!!
for run in range(100):
    players[0].forward(randint(1, 5))
    players[1].forward(randint(1, 5))
    players[2].forward(randint(1, 5))
    players[3].forward(randint(1, 5))


# 게임 끝========================
score_x = [0, 0, 0, 0]
score_y = [0, 0, 0, 0]

for i in range(4):
    score_x[i], score_y[i] = players[i].position()


#게임 끝 : 거북이 선수 이름 쓰기-------------
for i in range(4):
    t.penup()
    t.goto(score_x[i] + 20, score_y[i])
    t.pendown()
    t.write(name[i], align='left', font=('Arial', 12, 'normal'))

t.hideturtle() #커서 감추기

#게임 끝: 가장 많이 뛴 거북이 찾기-------------
maxValue = score_x[0]
max_i = 0
for i in range(1, len(score_x)):
    if maxValue < score_x[i]:
        maxValue = score_x[i]
        max_i = i

print("%s님, 1등입니다! 축하합니다!!" %name[max_i])


















