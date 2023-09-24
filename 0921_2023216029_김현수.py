Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code05-04.py ==========
100보다 크군요.
거짓이면 이 문장도 보이겠죠?
프로그램 끝

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code05-05.py ==========
정수를 입력하세요:  125
홀수를 입력했군요. 

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code05-06.py ==========
50보다 크고 100보다 작군요.

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code05-08.py ==========
점수를 입력하세요 : 100
A
학점입니다. ^^
for i in range(0, 3, 1) :
    print("%d : 안녕하세요? for 문을 공부 중입니다. ^^" %i)

    
0 : 안녕하세요? for 문을 공부 중입니다. ^^
1 : 안녕하세요? for 문을 공부 중입니다. ^^
2 : 안녕하세요? for 문을 공부 중입니다. ^^
for i in range(0,3):
    print("%d : 안녕하세요? for문을 공부 중입니다."%i)

    
0 : 안녕하세요? for문을 공부 중입니다.
1 : 안녕하세요? for문을 공부 중입니다.
2 : 안녕하세요? for문을 공부 중입니다.
for i in range(2, -1 ,-1):
    print("%d : 안녕하세요? for 문을 공부 중입니다. ^^"%i)

    
2 : 안녕하세요? for 문을 공부 중입니다. ^^
1 : 안녕하세요? for 문을 공부 중입니다. ^^
0 : 안녕하세요? for 문을 공부 중입니다. ^^
for i in range(1, 6, 1):
    print("%d"% i, end = " ")

    
1 2 3 4 5 

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-02(2).py ========
1에서 10까지의 합계 : 55

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-03.py ==========
500과 1000사이에 있는 홀수의 합계 : 187500

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-04.py ==========
값을 입력하세요 : 100
1에서 100까지의 합계: 5050

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-05.py ==========
시작값을 입력하세요 : 2
끝값을 입력하세요 : 300
증가값을 입력하세요 : 3
2에서 300까지 3씩 증가시킨 값의 합계 : 15050
i, dan = 0, 0
dan = int(input("단을 입력하세요: "))
단을 입력하세요: 7
for
SyntaxError: incomplete input
for i in range(1,10,1) :
    print("%d X %d = %2d" % (dan, i, dan * i))

    
7 X 1 =  7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
for i in range(0, 3, 1) :
    for k in range(0,2,1) :
        print("파이썬은 꿀잼입니다. ^^(i값 : %d, k값 : %d)"%(i, k))

        
파이썬은 꿀잼입니다. ^^(i값 : 0, k값 : 0)
파이썬은 꿀잼입니다. ^^(i값 : 0, k값 : 1)
파이썬은 꿀잼입니다. ^^(i값 : 1, k값 : 0)
파이썬은 꿀잼입니다. ^^(i값 : 1, k값 : 1)
파이썬은 꿀잼입니다. ^^(i값 : 2, k값 : 0)
파이썬은 꿀잼입니다. ^^(i값 : 2, k값 : 1)

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-07.py ==========
## 2단 ##
2 X 1 =  2
2 X 2 =  4
2 X 3 =  6
2 X 4 =  8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18

## 3단 ##
3 X 1 =  3
3 X 2 =  6
3 X 3 =  9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27

## 4단 ##
4 X 1 =  4
4 X 2 =  8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36

## 5단 ##
5 X 1 =  5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45

## 6단 ##
6 X 1 =  6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54

## 7단 ##
7 X 1 =  7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63

## 8단 ##
8 X 1 =  8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72

## 9단 ##
9 X 1 =  9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81


========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-08.py ==========
# 2단 ## 3단 ## 4단 ## 5단 ## 6단 ## 7단 ## 8단 ## 9단 #
 2X  1 =  2 3X  1 =  3 4X  1 =  4 5X  1 =  5 6X  1 =  6 7X  1 =  7 8X  1 =  8 9X  1 =  9
 2X  2 =  4 3X  2 =  6 4X  2 =  8 5X  2 = 10 6X  2 = 12 7X  2 = 14 8X  2 = 16 9X  2 = 18
 2X  3 =  6 3X  3 =  9 4X  3 = 12 5X  3 = 15 6X  3 = 18 7X  3 = 21 8X  3 = 24 9X  3 = 27
 2X  4 =  8 3X  4 = 12 4X  4 = 16 5X  4 = 20 6X  4 = 24 7X  4 = 28 8X  4 = 32 9X  4 = 36
 2X  5 = 10 3X  5 = 15 4X  5 = 20 5X  5 = 25 6X  5 = 30 7X  5 = 35 8X  5 = 40 9X  5 = 45
 2X  6 = 12 3X  6 = 18 4X  6 = 24 5X  6 = 30 6X  6 = 36 7X  6 = 42 8X  6 = 48 9X  6 = 54
 2X  7 = 14 3X  7 = 21 4X  7 = 28 5X  7 = 35 6X  7 = 42 7X  7 = 49 8X  7 = 56 9X  7 = 63
 2X  8 = 16 3X  8 = 24 4X  8 = 32 5X  8 = 40 6X  8 = 48 7X  8 = 56 8X  8 = 64 9X  8 = 72
 2X  9 = 18 3X  9 = 27 4X  9 = 36 5X  9 = 45 6X  9 = 54 7X  9 = 63 8X  9 = 72 9X  9 = 81

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-09.py ==========
1에서 10까지의 합계 : 55

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 55
더할 두 번째 수를 입력하세요 : 22
55 + 22 = 77
더할 첫 번째 수를 입력하세요 : 77
더할 두 번째 수를 입력하세요 : 128
77 + 128 = 205
더할 첫 번째 수를 입력하세요 : 0
0을 입력해 반복문을 탈출했습니다.

========== RESTART: C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 3
더할 두 번째 수를 입력하세요 : 2
3 + 2 = 5
더할 첫 번째 수를 입력하세요 : $
Traceback (most recent call last):
  File "C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py", line 5, in <module>
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: '$'

========== RESTART: C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 3
더할 두 번째 수를 입력하세요 : 2
3 + 2 = 5
더할 첫 번째 수를 입력하세요 : $
Traceback (most recent call last):
  File "C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py", line 5, in <module>
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: '$'

========== RESTART: C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 3
더할 두 번째 수를 입력하세요 : 2
3 + 2 = 5
더할 첫 번째 수를 입력하세요 : $
Traceback (most recent call last):
  File "C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py", line 5, in <module>
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: '$'

========== RESTART: C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 3
더할 두 번째 수를 입력하세요 : 2
Traceback (most recent call last):
  File "C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py", line 10, in <module>
    hap = a + b
TypeError: can only concatenate str (not "int") to str

========== RESTART: C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 3
더할 두 번째 수를 입력하세요 : 2
3 + 2 = 5
더할 첫 번째 수를 입력하세요 : $
$를 입력하여 반복문을 탈출했습니다.

========== RESTART: C:\Users\pc\Documents\오픈소스 프로그래밍_김현수\Code06-12.py ==========
더할 첫 번째 수를 입력하세요 : 3
더할 첫  번째 수를 입력하세요 : 2
3 + 2 = 5
더할 첫 번째 수를 입력하세요 : 5
더할 첫  번째 수를 입력하세요 : 5
5 + 5 = 10
더할 첫 번째 수를 입력하세요 : $
$를 입력하여 반복문을 탈출했습니다.

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-14.py ==========
1~100의 합계(3의 배수 제외) : 3367

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-15.py ==========
        ★
      ★★★
    ★★★★★
  ★★★★★★★
★★★★★★★★★
 ★★★★★★★
  ★★★★★
   ★★★
    ★
>>> 
========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code06-15.py ==========
        ★
      ★★★
    ★★★★★
  ★★★★★★★
★★★★★★★★★
  ★★★★★★★
    ★★★★★
      ★★★
        ★
>>> import turtle
>>> turtle.shape("turtle")
>>> 
>>> turtle.forward(100)
>>> turtle.right(90)
>>> turtle.forward(200)
>>> import turtle
>>> turtle.shape("turtle")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    turtle.shape("turtle")
  File "<string>", line 5, in shape
turtle.Terminator
>>> turtle.reset()
>>> for i in range(60):
...     turtle.circle(120)
...     turtle.right(360/60)
... 
...     
