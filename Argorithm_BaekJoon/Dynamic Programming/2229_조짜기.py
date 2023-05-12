N = int(input())
students = list(map(int,input().split()))
dp = [0 for i in range(len(students))]

for i in range(1, N): # 현재 i 가 1 이라면 
    tmpList = []
    for j in range(0,i+1): # j 의 range (0 1) 인 상황이고
        maxVal = max(students[i-j:i+1]) 
        minVal = min(students[i-j:i+1])
        subVal = maxVal - minVal
        if j == i :
            tmpList.append(subVal)
        else :
            tmpList.append(dp[i-j-1] + subVal)
        
    dp[i] = max(tmpList)        

print(dp[-1])



#      0 1 2 3 4 5 6 7 8 9
#      2 5 7 1 3 4 8 6 9 3
#      0 0 0 0 0 0 0 0 0 0 