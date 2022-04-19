from collections import deque

def freeze(cheeze,visit):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    dq = deque()
    dq.append([0,0])
    visit[0][0] = True
    while dq:
        x,y = dq.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<row and 0<=ny<col and visit[nx][ny] == False:
                if cheeze[nx][ny] >= 1:
                    cheeze[nx][ny] += 1
                else:
                    visit[nx][ny] = True
                    dq.append([nx,ny])

row,col = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(row)]
time = 0

while True:
    visit = [[False]*col for _ in range(row)]
    freeze(cheeze, visit)
    cnt = 0
    for i in range(row):
        for j in range(col):
            if cheeze[i][j] >= 3:
                cheeze[i][j] = 0
                cnt = 1
            elif cheeze[i][j] == 2:
                cheeze[i][j] = 1
    if cnt == 1:
        time += 1
    else:
        break

print(time)