pr = int(input())
a = 0

if pr != 0:
    curNum = int(input())
    while curNum != 0:
        if curNum > pr:
            a += 1
        pr = curNum
        curNum = int(input())

print(a)
