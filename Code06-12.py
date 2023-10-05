hap = 0
a, b = 0, 0

while True :
    a = input("더할 첫 번째 수를 입력하세요 : ")
    if a == '$' :
        print("$를 입력하여 반복문을 탈출했습니다.")
        break
    else :
        a = int(a)
    b = int(input("더할 첫  번째 수를 입력하세요 : "))
    hap = int(a) + b
    print("%d + %d = %d" % (int(a), b, hap))


