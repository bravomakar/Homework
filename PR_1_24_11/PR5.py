a = int(input())
if a == 0:
    print(0)
else:
    max = 1
    curLen = 1
    
    curNum = int(input())
    while curNum != 0:
        if curNum == a:
            curLen += 1
        else:
            curLen = 1
        
        # Проверяем рекорд на каждом шаге
        if curLen > max:
            max = curLen
            
        a = curNum
        curNum = int(input())
        
    print(max)
