# from collections import deque
# n,m = map(int, input().split())
# miro = []
# for i in range(m):
#     miro.append(list(map(int,input())))
# answer = [[0]*n for _ in range(m)]
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# dq = deque()
# dq.append((0,0,0))
# while dq:
#     col,row,cnt = dq.popleft()
#     for i in range(2):
#         tx = col + dx[i]
#         ty = row + dy[i]
#         if 0<=tx<n and 0<=ty<m:
#             if miro[ty][tx] == 1 and answer[ty][tx] == 0 :
#                 dq.append((ty,tx,cnt+1))
#                 answer[ty][tx] = cnt+1
#             elif miro[ty][tx] == 1 and answer[ty][tx] >= cnt+1 :
#                 dq.append((ty,tx,cnt+1))
#                 answer[ty][tx] = cnt+1
#             elif miro[ty][tx] == 0 and answer[ty][tx] == 0 :
#                 dq.append((ty,tx,cnt))
#                 answer[ty][tx] = cnt
#             elif miro[ty][tx] == 0 and answer[ty][tx] != 0 : 
#                 dq.append((ty,tx,min(answer[ty][tx], cnt)))
#                 answer[ty][tx] = min(answer[ty][tx], cnt)
# print(answer[m-1][n-1])


import heapq
m, n = map(int, input().split())
miro = []
visit =[[False] * m for _ in range(n)]

for i in range(n):
    miro.append(list(map(int, input().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
heap = []
heapq.heappush(heap, (0, 0, 0))
visit[0][0] = True
while heap:
    wallCount, x, y = heapq.heappop(heap)
    if x == n - 1 and y == m - 1:
        print(wallCount)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == False:
            if miro[nx][ny] == 1:
                heapq.heappush(heap, (wallCount+1, nx, ny))
            else:
                heapq.heappush(heap, (wallCount, nx, ny))
            visit[nx][ny] = True