from collections import deque
import sys
input = sys.stdin.readline
 
def bfs(x, y, rained_line):  
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1	
 
    while queue:
        x, y = queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] >= rained_line and visited[nx][ny] == 0:    
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
 
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
lowest_point = min(map(min, graph))    
highest_point = max(map(max, graph))    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
max_safe_area = 0
for rained_line in range(lowest_point, highest_point+1):
    visited = [[0] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= rained_line and visited[i][j] == 0:
                bfs(i, j, rained_line)
                tmp += 1
    if tmp > max_safe_area:    
        max_safe_area = tmp
print(max_safe_area)