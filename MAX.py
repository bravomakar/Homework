from math import *


x = int(input())

a=x//100
b=x%100 // 10
c=x%10

if (a+b+c) % 2 == 0:
    print(True)
else:
    print(False)