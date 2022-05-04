from collections import deque
N,M=map(int,input().split(" "))
graph = [[0 for i in range(M)] for j in range(N)]
for k in range(N):
    graph[k]=list(map(int, str(input())))
visit = [[False for i in range(M)] for j in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def miro(a,b):
    q = deque()
    q.append((a,b,1))
    visit[a][b]=True
    while q:
        a,b,count = q.popleft()
        if a==N-1 and b==M-1:
            print(count)
            break
        for i in range(4):
            tx = b + dx[i]
            ty = a + dy[i]
            if 0<=tx<M and 0<=ty<N and visit[ty][tx]==False and graph[ty][tx]==1:
                q.append((ty,tx,count+1))
                visit[ty][tx]=True
miro(0,0)