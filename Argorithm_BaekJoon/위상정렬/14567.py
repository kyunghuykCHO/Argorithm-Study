import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0] * (N+1)
minSemester = [0] * (N+1)
graph = defaultdict(list)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

dq = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        dq.append(i)
        minSemester[i] = 1

while dq:
    n = dq.popleft()
    for i in graph[n]:
        degree[i] -= 1
        minSemester[i] = max(minSemester[n] + 1, minSemester[i])
        if degree[i] == 0:
            dq.append(i)

print(*minSemester[1:])