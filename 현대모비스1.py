# 현대모비스 알고리즘 경진대회 예선 문제 -- 생선공정 
from collections import deque
factory = []
result = deque()
N = int(input())
for _ in range(N):
    factory.append(input()) 
K = int(input())
for _ in range(K):
    result.append(input())
answer = [[0]*2 for _ in range(K)]
cnt =  0
while result:
    res = result.popleft()
    flag = 1
    for item in factory:
        if len(item) >= len(res) and item[:len(res)] == res:
            if flag == 1:
                answer[cnt][0] = item
                answer[cnt][1] = 1
                flag = 0 
                continue
            if len(item) > len(answer[cnt][0]) :
                answer[cnt][0] = item 
                answer[cnt][1] = 1
            elif item == answer[cnt][0] : 
                answer[cnt][1] += 1
    cnt+=1
print("============ RESULT =============")
for i in range(len(answer)):
    if answer[i][0] != 0 :
        print(answer[i][0] , answer[i][1])
    else :
        print(0)