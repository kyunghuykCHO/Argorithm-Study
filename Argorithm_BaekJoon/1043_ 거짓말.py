from collections import deque

N,M = map(int,input().split())
know = [False for _ in range(N+1)]
tmp = list(map(int,input().split()))
dq = deque([])
if tmp[0]!=0:
    for i in range(1,len(tmp)):
        know[tmp[i]] = True
        dq.append(tmp[i])

graph = []
for i in range(M):
    a = list(map(int,input().split()))
    graph.append(a[1:])

while dq:
    search = dq.popleft()
    for j in graph:
        line = j
        for k in j:
            if know[k] == True:
                for l in line:
                    if know[l]==False:
                        know[l] = True
                        dq.append(l)

result = 0
for m in graph:
    cnt = 0
    for n in m:
        if know[n]==True:
            cnt+=1
    if cnt== 0:
        result+=1   

print(result)

