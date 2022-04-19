from collections import deque

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    global cnt
    cnt+=1
    dq = deque()
    dq.append((x,y))
    count = 0
    A[x][y] = 2
    while dq:
        x,y = dq.popleft()
        count+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and A[nx][ny] == 1:
                dq.append((nx,ny))
                # ★★★★★★★★★★★★★★★★★★★★★★★★
                A[nx][ny] = 2
                # ★★★★★★★★★★★★★★★★★★★★★★★★
    cnt_A.append(count)

cnt = 0
cnt_A = []
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == 1:
            bfs(i,j)

print(cnt)
for k in sorted(cnt_A):
    print(k)