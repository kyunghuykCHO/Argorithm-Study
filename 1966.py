from collections import deque
T = int(input())
for i in range(T):
    lstLen, idx = map(int, input().split())
    dq = deque(list(map(int, input().split())))
    count = 0
    while dq:
        maxValue = max(dq)  
        num = dq.popleft() 
        idx -= 1 
        if maxValue == num: 
            count += 1 
            if m < 0: 
                print(count)
                break
        else:   
            dq.append(num) 
            if m < 0 :  
                m = len(dq) - 1 
                
                
       
            