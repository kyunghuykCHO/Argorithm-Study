from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque([])
row, col = map(int,input().split())
cheezes = []
freezedCheeze = 0
count = 0
melted = 0
for i in range(row):
    line = list(map(int, input().split()))
    for j in range(col):
        if line[j]==1 : 
            freezedCheeze += 1
    cheezes.append(line)

def bfs(r,c):
    meltedCheeze = 0
    visited = [[False] * col for _ in range(row)]
    dq.append((r,c))
    visited[r][c] = True
    while dq:
        r,c = dq.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<row and 0<=nc<col and visited[nr][nc]==False:
                if cheezes[nr][nc] == 0 :
                    dq.append((nr,nc)) 
                    visited[nr][nc] = True
                elif cheezes[nr][nc] == 1 :
                    cheezes[nr][nc] = 0
                    visited[nr][nc] = True
                    meltedCheeze += 1
    return meltedCheeze

while True:
    prevMelted = melted
    melted = bfs(0,0)
    count += 1
    if melted == 0 :
        print(count-1)
        print(prevMelted)
        break

