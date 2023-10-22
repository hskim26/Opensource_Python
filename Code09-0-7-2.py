def func1():
    global a
    a = 'Hi'
    print("func1()에서 a값 %s" %a)

def func2():
    print("func2()에서 a값 %s" %a)

def func3():
    print("메인 끝에서 a값 %s" %a)

a=20

print("메인 시작에서 a값 %d" %a)

func1()
func2()
func3()


