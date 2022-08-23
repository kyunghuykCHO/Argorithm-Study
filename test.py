from collections import deque


dqq = deque()
dq = deque()
dq.append((1,2,3))
dqq.append((1,dq))
print(dqq)