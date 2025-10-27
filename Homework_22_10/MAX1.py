a=int(input())
b=int(input())
c=int(input())

if (a != b and b != c and a != c) and ((a + b > c) and (a + c > b) and (b + c > a)):
    print(True)
else:
    print(False)

