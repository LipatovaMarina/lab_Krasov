import math
flag = "+"
while flag == "+":
    print("Введите а")
    a = int(input())
    print("Введите b")
    b = int(input())
    print("Введите с")
    c = int(input())
    D = b*b-4*a*c
    if a == 0:
        if b > 0:
            x1 = (-c)/(b)
            print("x = ", x1, "Продолжить? (+/-)")
            flag = input()
        elif b == 0:
            print("Уравнение не квадратное. Продолжить? (+/-)")
            flag = input()
        continue
    if D > 0:
        x1 = (-b+math.sqrt(D))/(2*a)
        x2 = (-b-math.sqrt(D))/(2*a)
        print("x1 = ",x1)
        print("x2 = ",x2, "Продолжить? (+/-)")
        flag = input()
        continue
    elif D == 0:
        x1=(-b)/(2*a)
        x2=(-b)/(2*a)
        print("x1, x2 = ", x1, "Продолжить? (+/-)")
        flag = input()
        continue
    elif D < 0:
        print("Дискриминант меньше 0, (D=",D,"), Продолжить? (+/-)")
        flag = input()
        continue