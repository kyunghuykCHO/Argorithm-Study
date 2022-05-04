import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input())
S = []
for i in range(N):
    S.append(list(input().rstrip()))
V = [[False]*N for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y) :
    ccolor = S[x][y]
    V[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and V[nx][ny] == False and S[nx][ny] == ccolor:
            bfs(nx,ny)

no_weak = 0
for i in range(len(S)):
    for j in range(len(S[0])):
        if V[i][j] == False:
            bfs(i,j)
            no_weak += 1
weak = 0

for i in range(len(S)):
    for j in range(len(S[0])):
        if S[i][j] == 'R':
            S[i][j] = 'G'

V = [[False]*N for i in range(N)]
for i in range(len(S)):
    for j in range(len(S[0])):
        if V[i][j] == False:
            bfs(i,j)
            weak += 1

print(no_weak ,weak)