def para_func(*para):
    result=0
    i=0
    for num in para:
        i+=1
        result += num

    return result, i

hap = 0
n=0

hap, n = para_func(10, 20)
print("매개변수가 %d개인 함수를 호출한 결과 ==> %d" %(n, hap))
hap, n = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("매개변수가 %d개인 함수를 호출한 결과 ==> %d" %(n,hap))
