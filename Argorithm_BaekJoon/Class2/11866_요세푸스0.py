from collections import deque
N,K = map(int,input().split())
people = deque([])
for _ in range(1,N+1):
    people.append(_)
result = []
while people:
    for i in range(K-1):
        tmp = people.popleft()
        people.append(tmp)
    result.append(people.popleft())
print("<",end="")
for j in range(len(result)):
    if j==len(result)-1:
        print(result[j],end=">")
    else:
        print(result[j],end=", ")