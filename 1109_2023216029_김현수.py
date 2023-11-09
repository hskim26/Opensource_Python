Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\1\Desktop\Module1.py
def func1():
    print("Module1.py의 func1()이 호출됨.")

    
Module1.func1()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Module1.func1()
NameError: name 'Module1' is not defined
Module1.py
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Module1.py
NameError: name 'Module1' is not defined
import Module1
Module1.func1()
Module1.py의 func1()이 호출됨.

======================= RESTART: C:/Users/1/Desktop/A.py =======================
Module1.py의 func1()이 호출됨.
Module1.py의 func2()이 호출됨.
Module1.py의 func3()이 호출됨.

======================= RESTART: C:/Users/1/Desktop/B.py =======================
Module1.py의 func1()이 호출됨.
Module1.py의 func2()이 호출됨.
Module1.py의 func3()이 호출됨.

==================== RESTART: C:/Users/1/Desktop/myTurtle.py ===================

=================== RESTART: C:/Users/1/Desktop/Code09-14.py ===================
st = getString()
print(st)
Python~!
Exception ignored in: <function Image.__del__ at 0x0000020F062559E0>
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1776.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 4080, in __del__
    self.tk.call('image', 'delete', self.name)
RuntimeError: main thread is not in main loop

================================ RESTART: Shell ================================
def hap(num1, num2):
    res = num1 + num2
    return res

print(hap(10,20))
30
hap2 = lamda num1, num2 : num1 + num2
SyntaxError: invalid syntax
hap2 = lambda num1, num2 : num1 + num2
print(hap2(10,20))
30
hap3 = lambda num1 = 10, num2 = 20: num1 + num2
print(hap3())
30
print(hap3(100,200))
300
myList = [1, 2, 3, 4, 5]
def add10(num):
    return num + 10

for i in range(len(myList)):
    myList[i] = add10(myList[i])
print(myList)
SyntaxError: invalid syntax
print(myList)
[1, 2, 3, 4, 5]
myList = [1, 2, 3, 4, 5]
add10 = lambda num : num + 10
myList = list(map(add10, myList))
print(myList)
[11, 12, 13, 14, 15]
myList = [1, 2, 3, 4, 5]
myList = list(map(lambda num : num + 10, myList))
print(myList)
[11, 12, 13, 14, 15]
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40]
hapList = list(map(lambda n1, n2 : n1 + n2, list1, list2))
print(hapList)
[11, 22, 33, 44]
def count(num):
    if num >= 1:
        print(num, end = '')
        count(num - 1)
    else :
        return

count(10)
10987654321
count(20)
2019181716151413121110987654321
def count(num):
    if num >= 1:
        print(num , end = '')
        count(num - 1)
    else :
        return

    
count(10)
10987654321
count(20)
2019181716151413121110987654321
>>> def count(num):
...     if num >= 1:
...         print(num , end = ' ')
...         count(num - 1)
...     else :
...         return
... 
...     
>>> count(10)
10 9 8 7 6 5 4 3 2 1 
>>> count(20)
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
>>> def factorial(num):
...     print("factorial(%d) 호출" %num)
...     if num <= 1:
...         return num
...     else :
...         return num * factorial(num - 1)
... 
...     
>>> factorial(4)
factorial(4) 호출
factorial(3) 호출
factorial(2) 호출
factorial(1) 호출
24
>>> factorial(10)
factorial(10) 호출
factorial(9) 호출
factorial(8) 호출
factorial(7) 호출
factorial(6) 호출
factorial(5) 호출
factorial(4) 호출
factorial(3) 호출
factorial(2) 호출
factorial(1) 호출
3628800
