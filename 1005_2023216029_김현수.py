Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02.py ==========
1번째 숫자: 10
2번째 숫자: 20
3번째 숫자: 30
4번째 숫자: 40
합계 ==> 100

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(1).py ========
[0, 0, 0, 0]
aa=[]
for i in range(0, 100):
    aa.append(0)
len(aa)
SyntaxError: invalid syntax

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py", line 4, in <module>
    Len(aa)
NameError: name 'Len' is not defined. Did you mean: 'len'?

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========

========= RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-02(2).py ========
100

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-03.py ==========
10번째 숫자: 10
10번째 숫자: 10
10번째 숫자: 
Traceback (most recent call last):
  File "C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-03.py", line 8, in <module>
    aa[i] = int(input(str(i+1) + "번째 숫자: "))
ValueError: invalid literal for int() with base 10: ''


========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-03.py ==========
1번째 숫자: 10
2번째 숫자: 20
3번째 숫자: 30
4번째 숫자: 40
5번째 숫자: 50
6번째 숫자: 60
7번째 숫자: 70
8번째 숫자: 80
9번째 숫자: 90
10번째 숫자: 100
합계 ==> 550

======== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/그림7-3을 코드로 구현.py ========
bb[0]에는 198이, bb[99]에는 0이 입력됩니다.
aa=[10, 20, 30, 40]
aa[0:3]
[10, 20, 30]
aa[2:4]
[30, 40]
aa=[10, 20, 30]
bb=[40, 50, 60]
aa + bb
[10, 20, 30, 40, 50, 60]
aa*3
[10, 20, 30, 10, 20, 30, 10, 20, 30]
aa=[10, 20, 30, 40, 50, 60, 70]
aa[::2]
[10, 30, 50, 70]
aa[::-2]
[70, 50, 30, 10]
aa[::-1]
[70, 60, 50, 40, 30, 20, 10]
aa=[10, 20, 30]
aa[1:2]=[200,201]
aa
[10, 200, 201, 30]
aa=[10, 20, 30]
del(aa[1])
aa
[10, 30]
aa=[10, 20, 30, 40, 50]
aa[1:4]=[]
aa
[10, 50]

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-05.py ==========
현재 리스트: [30, 10, 20]
append(40)후의 리스트 : [30, 10, 20, 40]
pop()으로 추출한 값: 40
pop()후의 리스트: [30, 10, 20]
sort()후의 리스트: [10, 20, 30]
20값의 위치 : 1
insert(2, 222)후의 리스트 : [10, 20, 222, 30]
remove(222) 후의 리스트 : [10, 20, 30]
extend([77, 88, 77]) 후의 리스트 : [10, 20, 30, 77, 88, 77]
77값의 개수: 2

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-06.py ==========
  1  2  3  4
  5  6  7  8
  9 10 11 12
tt1=(10, 20, 30); tt1
(10, 20, 30)
tt2=10, 20, 30; tt2
(10, 20, 30)
tt1.append(40)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tt1.append(40)
AttributeError: 'tuple' object has no attribute 'append'
tt1[0]=40
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tt1[0]=40
TypeError: 'tuple' object does not support item assignment
del(tt1[0])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del(tt1[0])
TypeError: 'tuple' object doesn't support item deletion
tt1 = (10, 20, 30, 40)
tt1[0]
10
tt1[0] + tt1[1] + tt1[2]
60
tt2=('A', 'B')
tt1 + tt2
(10, 20, 30, 40, 'A', 'B')
tt2*3
('A', 'B', 'A', 'B', 'A', 'B')
myTuple = (10, 20, 30)
myList = list(myTuple)
myList = list(myTuple)
myList.append(40)
myTuple=tuple(myList)
myTuple
(10, 20, 30, 40)
dic1={1 : 'a', 2: 'b', 3: 'c'}
dic1
{1: 'a', 2: 'b', 3: 'c'}
student1={'학번' : 1000, '이름' : '홍길동', '학과': '컴퓨터학과'}
student1
{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
student1['연락처'] = '010-1111-2222'
student1
{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과', '연락처': '010-1111-2222'}
student1['학과
         
SyntaxError: incomplete input
student1['학과']='파이썬학과'
         
student1
         
{'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '연락처': '010-1111-2222'}
del[student['학과'])
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
del(student['학과'])
         
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    del(student['학과'])
NameError: name 'student' is not defined. Did you mean: 'student1'?
del(student1['학과'])
         
student1
         
{'학번': 1000, '이름': '홍길동', '연락처': '010-1111-2222'}
studen1 = {'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '학번': 2000}
         
student1
         
{'학번': 1000, '이름': '홍길동', '연락처': '010-1111-2222'}
student1['학번']
         
1000
student1 = {'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '학번': 2000}
         
student1
         
{'학번': 2000, '이름': '홍길동', '학과': '파이썬학과'}
student1['학번']
         
2000
student1['이름']
         
'홍길동'
student1['학과']
         
'파이썬학과'
list(student1.keys())
         
['학번', '이름', '학과']
student1.items()
         
dict_items([('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과')])

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-08.py ==========
이름 --> 트와이스
구성원 수 --> 9
데뷔 --> 서바이벌 식스틴
대표곡 --> SIGNAL

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-09.py ==========
[('Edward', '에드워드'), ('Gothen', '고든'), ('Henry', '헨리'), ('James', '제임스'), ('Thomas', '토마스')]

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code07-10.py ==========
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?<치킨> 궁합 음식은 <치킨무>입니다.
그런 음식이 없습니다.확인해 보세요.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?치킨
<치킨> 궁합 음식은 <치킨무>입니다.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?라면
<라면> 궁합 음식은 <김치>입니다.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?짬뽕
그런 음식이 없습니다.확인해 보세요.
['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살'] 중 좋아하는 음식은?끝
mySet1={1, 2, 3, 4, 5}
         
mySet2={4, 5, 6, 7}
         
mySet1 & mySet2
         
{4, 5}
mySet|mySet2
         
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    mySet|mySet2
NameError: name 'mySet' is not defined. Did you mean: 'mySet1'?
mySet1 || mySet2
         
SyntaxError: invalid syntax
mySet1 | mySet2
         
{1, 2, 3, 4, 5, 6, 7}
mySet1 = mySet2
         
mySet1 = {1, 2, 3, 4, 5}
         
mySet2 = {4, 5, 6, 7}
         
mySet1 - mySet2
         
{1, 2, 3}
mySet1 ^ mySet2
         
{1, 2, 3, 6, 7}
numList = [num*num for num in range(1,6)]
         
numList
         
[1, 4, 9, 16, 25]
>>> numList = [num for num in range(1, 21)if num % 3 == 0]
...          
>>> numList
...          
[3, 6, 9, 12, 15, 18]
>>> foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
...          
>>> sides = ['오뎅', '단무지
...          
SyntaxError: incomplete input
>>> sides = ['오뎅', '단무지', '김치']
...          
>>> for foodm side in zip(foods, sides):
...          
SyntaxError: invalid syntax
>>> for food, side in zip(foods, sides):
...          print(food, '-->', side)
... 
...          
떡볶이 --> 오뎅
짜장면 --> 단무지
라면 --> 김치
>>> foods=['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
...          
>>> side=['오뎅', '단무지', '김치']
...          
>>> tupList = lsit(zip(foods, sides))
...          
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    tupList = lsit(zip(foods, sides))
NameError: name 'lsit' is not defined
d
>>> tupList = list(zip(foods, sides))
...          
>>> dic = dict(zip(foods, sides))
...          
>>> tupList
...          
[('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치')]
>>> dic
...          
{'떡볶이': '오뎅', '짜장면': '단무지', '라면': '김치'}
