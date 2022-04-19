from collections import deque

def bfs(dq, tomatoes):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                dq.append([nx, ny])

M,N = map(int,input().split())
tomatoes = []
for i in range(N):
    tomatoes.append(list(map(int,input().split())))

dq = deque([])
for j in range(N):
    for k in range(M):
        if tomatoes[j][k] == 1 :
            dq.append([j,k])

bfs(dq, tomatoes)

result = 0
for k in tomatoes:
    for l in k:
        if l == 0:
            print(-1)
            exit()
    result = max(result, max(k))
print(result - 1)
    
