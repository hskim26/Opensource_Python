Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("100+100")
100+100
print("%d" % (100 + 100))
200
print("%d" % (100, 200))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("%d" % (100, 200))
TypeError: not all arguments converted during string formatting
print("%d %d" % (100))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("%d %d" % (100))
TypeError: not enough arguments for format string
print("%d %d" % (100, 200))
100 200
print("%d %5d %05d" % (123, 123, 123))
123   123 00123
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
123   123 00123
print("{2:d} {1:d} {0:d}".format(100, 200, 300))
300 200 100
bin(11); bin(0o11); bin(0x11)
'0b1011'
'0b1001'
'0b10001'
oct(11); oct(0b11); oct(0x11)
'0o13'
'0o3'
'0o21'
hex(11); hex(0b11); hex(0o11)
'0xb'
'0x3'
'0x9'

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code03-04.py ==========
입력 진수 결정(16/10/8/2) : 16
값 입력 : FF
16진수 ==> 0xff
10진수 ==> 255
8진수 ==> 0o377
2진수 ==> 0b11111111
a = 123
type(a)
<class 'int'>
a = 100**100
print(a)
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
a = 10; b = 20
print(a + b,a - b,a * b, a / b)
30 -10 200 0.5
a = True
type(a)
<class 'bool'>
a = """파이썬
만세"""
a
'파이썬\n만세'
print(a)
파이썬
만세
a, b, c = 2, 3, 4
print(a + b - c, a + b * c, a * b / c)
1 14 1.5
s1, s2, s3 = "100", "100.123", "9999999999999999999999999"
print(int(s1) + 1,float(s2) + 1, int(s3) + 1)
101 101.123 10000000000000000000000000
a = 100; b = 100.123
str(a) + '1'; str(b) + '1'
'1001'
'100.1231'

========== RESTART: C:/Users/pc/Documents/오픈소스 프로그래밍_김현수/Code04-01.py ==========
교환할 돈은 얼마? 7777

 500원짜리 ==> 15개
 100원짜리 ==> 2개
 50원짜리 ==> 1개
 10원짜리 ==> 2개
 바꾸지 못한 잔돈 ==> 7원 

a = 99
(a > 100) and (a < 200)
False
(a > 100) or (a < 200)
True
not(a == 100)
True
if(1234) : print("참이면 보여요")
if(0) : print("거짓이면 안 보여요")
SyntaxError: invalid syntax
if(1234) : print("참이면 보여요")

참이면 보여요
>>> if(0) :
...     print("거짓이면 안 보여요")
... 
...     
>>> 10 & 7
2
>>> 123 & 456
72
>>> 0xFFFF & 0x0000
0
>>> 10 | 7
15
>>> 123 | 456
507
>>> 0xFFFF || 0x0000
SyntaxError: invalid syntax
>>> 0xFFFF | 0x0000
65535
>>> 10 ^ 7
13
>>> 123 ^ 456
435
>>> 0xFFFF ^ 0x0000
65535
>>> a = 12345
>>> ~a + 1
-12345
>>> a = 10
>>> a << 1; a << 2; a << 3; a << 4
20
40
80
160
>>> a = 10
>>> a >> 1; a >> 2; a >> 3; a >> 4
5
2
1
0
