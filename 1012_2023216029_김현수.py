Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ss="파이썬최고"
ss[0]
'파'
ss[1:3]
'이썬'
ss[3:]
'최고'

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01.py ==========
파$이$썬$짱$!$

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01-2.py =========
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01-2.py", line 3, in <module>
    print(result)
NameError: name 'result' is not defined

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01-2.py =========
!$

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01-2.py =========
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01-2.py", line 3, in <module>
    result=len(ss) + '$'
TypeError: unsupported operand type(s) for +: 'int' and 'str'

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-01-2.py =========
파$이$썬$짱$!$

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 8-1.py =======
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 8-1.py", line 7, in <module>
    if( ss[i]  % 2 == 0):
TypeError: not all arguments converted during string formatting

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-02.py ==========
문자열을 입력하세요 : 즐거운 Python 프로그래밍~~~
내용을 거꾸로 출력 --> ~~~밍래그로프 nohtyP 운거즐
ss = 'Python is Easy. 그래서 programming이 재미있습니다.^^'
ss.upper()
'PYTHON IS EASY. 그래서 PROGRAMMING이 재미있습니다.^^'
ss
'Python is Easy. 그래서 programming이 재미있습니다.^^'
ss.lower()
'python is easy. 그래서 programming이 재미있습니다.^^'
ss
'Python is Easy. 그래서 programming이 재미있습니다.^^'
ss.swapcase()
'pYTHON IS eASY. 그래서 PROGRAMMING이 재미있습니다.^^'
ss.title()
'Python Is Easy. 그래서 Programming이 재미있습니다.^^'
ss.capitalize()
'Python is easy. 그래서 programming이 재미있습니다.^^'
ss
'Python is Easy. 그래서 programming이 재미있습니다.^^'

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-03.py ==========
입력 문자열 ==>  파이썬 열공 중~~
출력 문자열 ==> ( 파이썬 열공 중~~)

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 8-1.py =======
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 8-1.py", line 7, in <module>
    if( ss[i]  % 2 != 0):
TypeError: not all arguments converted during string formatting
ss='열심히 파이썬 공부 중~~'
ss.replace('파이썬', 'Python')
'열심히 Python 공부 중~~'
ss='Python을 열심히 공부 중'
ss.split()
['Python을', '열심히', '공부', '중']
ss='하나:둘:셋'
ss.split(':')
['하나', '둘', '셋']
ss='하나\n둘\n셋'
ss.splitliness()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ss.splitliness()
AttributeError: 'str' object has no attribute 'splitliness'. Did you mean: 'splitlines'?
ss.splitlines()
['하나', '둘', '셋']
\
ss='%'
ss.join('파이썬')
'파%이%썬'

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-06.py ==========
날짜(연/월/일) 입력 ==> 2019/12/31
입력한 날짜의 10년 후 ==>2029년12월31일

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 8-1.py =======
파#썬#완#재#있#요
ss='열심히 파이썬 공부 중~~'
ss.replace('파이썬', 'Python')
'열심히 Python 공부 중~~'
ss = 'Python을 열심히 공부 중'
ss.split()
['Python을', '열심히', '공부', '중']
ss='하나:둘:셋'
ss.split(':')
['하나', '둘', '셋']
ss='하나\n둘\n셋'
ss.splitlines()
['하나', '둘', '셋']
ss='%'
ss.join('파이썬')
'파%이%썬'
before = ['2019', '12', '31']
after = list(map(int , before))
after
[2019, 12, 31]

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-07.py ==========

Warning (from warnings module):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-07.py", line 21
    tX = random.randrange(-swidth / 2, swidth /2)
DeprecationWarning: non-integer arguments to randrange() have been deprecated since Python 3.10 and will be removed in a subsequent version

Warning (from warnings module):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code08-07.py", line 22
    tY = random.randrange(-sheight/ 2, sheight / 2)
DeprecationWarning: non-integer arguments to randrange() have been deprecated since Python 3.10 and will be removed in a subsequent version
Exception ignored in: <function Image.__del__ at 0x0000020E16404CC0>
Traceback (most recent call last):
  File "C:\Users\pc\AppData\Local\Programs\Python\Python311\Lib\tkinter\__init__.py", line 4080, in __del__
    self.tk.call('image', 'delete', self.name)
RuntimeError: main thread is not in main loop

================================ RESTART: Shell ================================

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 8-2.py =======
원래 문자열 ==> [<<<파<<이>>썬>>>]
공백 삭제 문자열 ==> [파이썬]

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code09-04.py ==========
100과 200의 plus() 함수 결과는 300

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 9-2.py =======
첫 번째 수를 입력하세요 : 
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 9-2.py", line 21, in <module>
    var1 = int(input("첫 번째 수를 입력하세요 : "))
ValueError: invalid literal for int() with base 10: ''

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 9-2.py =======
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /): /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다.ㅠㅠ
계산불가
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 9-2.py", line 29, in <module>
    res = calc(var1, var2, oper)
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 9-2.py", line 11, in calc
    result = v1 / v2
ZeroDivisionError: division by zero

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY 9-2.py =======
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /): /
두 번째 수를 입력하세요 : 2
## 계산기 : 34 / 2 = 17

======= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py ======
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /): +
두 번째 수를 입력하세요 : 5
계속하려면 Y를 눌러주세요: 
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py", line 35, in <module>
    if continue_condition != 'y' and contine_condition != 'Y':
NameError: name 'contine_condition' is not defined. Did you mean: 'continue_condition'?

======= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py ======
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /): +
두 번째 수를 입력하세요 : 5
계속하려면 Y를 눌러주세요: 
## 계산기 : 34 + 5 = 39

======= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py ======
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /): +
두 번째 수를 입력하세요 : 5
## 계산기 : 34 + 5 = 39
계속하려면 Y를 눌러주세요: y
첫 번째 수를 입력하세요 : 33
계산을 입력하세요(+, -, *, /): /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다.ㅠㅠ
계산불가
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py", line 31, in <module>
    res = calc(var1, var2, oper)
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py", line 11, in calc
    result = v1 / v2
ZeroDivisionError: division by zero
>>> 
======= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/SELF-STUDY(y 반복).py ======
첫 번째 수를 입력하세요 : 34
계산을 입력하세요(+, -, *, /): +
두 번째 수를 입력하세요 : 5
## 계산기 : 34 + 5 = 39
계속하려면 Y를 눌러주세요: y
첫 번째 수를 입력하세요 : 33
계산을 입력하세요(+, -, *, /): /
두 번째 수를 입력하세요 : 0
0으로는 나누면 안됩니다.ㅠㅠ
계산불가
계속하려면 Y를 눌러주세요: Y
첫 번째 수를 입력하세요 : 23
계산을 입력하세요(+, -, *, /): **
두 번째 수를 입력하세요 : 3
## 계산기 : 23 ** 3 = 12167
계속하려면 Y를 눌러주세요: 
프로그램을 종료합니다.
