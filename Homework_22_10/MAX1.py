x = int(input())

'''a=x//100
b=x%100 // 10
c=x%10'''

if (a != b and b != c and a != c) and ((a + b > c) and (a + c > b) and (b + c > a)):
    print(True)
else:
    print(False)

Треугольник разносторонний.
