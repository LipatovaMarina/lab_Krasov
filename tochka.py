import math
x=float(input("введите x:"))
y=float(input("введите y:"))
if(y<k*x+b):
    if((x-xc)**2+(y-yc)**2<r**2):
        if(x1<x<x2) and (y1<y<y2):
            print("Обл.4")
    else:
        if(y>y2):
            print("Обл.5")
        else:
            print("Обл.6")
    else:
        if (x1 < x < x2) and (y1 < y < y2):
            print("Обл.7")
        else:
            print("Обл.8")
else:
    if ((x - xc) ** 2 + (y - yc) ** 2 < r ** 2):
        if (x1 < x < x2) and (y1 < y < y2):
            print("Обл.3")
        else:
            print("Обл.2")
    else:
        print("Обл.1")
print("Конец")