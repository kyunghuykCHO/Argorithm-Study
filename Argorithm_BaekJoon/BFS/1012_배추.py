'''

VISIT 그래프를 따로 만들지 않고 1,0 으로 된 그래프에서
방문한 index 는 0으로 초기화 하는 방식 ! 

'''

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    q = deque()
    q.append((x,y))
    visit[x][y]=True
    while q:
        a,b = q.popleft()
        for i in range(4):
            tx = b + dx[i]
            ty = a + dy[i]
            if 0<=tx<col and 0<=ty<row and visit[ty][tx]==False and field[ty][tx]==1:
                q.append((ty,tx))
                visit[ty][tx]=True

TestCase = int(input())
for i in range(TestCase):
    col,row,cabbages = map(int,input().split())
    field = [[0 for j in range(col)] for k in range(row)]
    for l in range(cabbages):
        x,y = map(int,input().split())
        field[y][x] = 1
    visit = [[False for o in range(col)] for p in range(row)]
    count=0
    for m in range(row):
        for n in range(col):
            if field[m][n]==1 and visit[m][n]==False:
                bfs(m,n)
                count+=1
    print(count)
