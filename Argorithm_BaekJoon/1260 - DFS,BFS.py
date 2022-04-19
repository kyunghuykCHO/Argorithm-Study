# from collections import deque

# N,M,V = map(int, input().split())
# # N : 정점의 개수 M : 간선의 개수 V : 탐색 시작 정점
# V= V-1

# graph = [[0 for i in range(N)] for j in range(N)]
# DFS_visit = [False for k in range(N)]
# BFS_visit = [False for l in range(N)]

# for i in range(M):
#     row,col = map(int,input().split())
#     graph[row-1][col-1] = 1
#     graph[col-1][row-1] = 1

# def dfs(V):
#     DFS_visit[V] = True
#     print(V+1,end=" ")
#     for i in range(N):
#         if DFS_visit[i]==False and graph[V][i]==1:
#             dfs(i)

# def bfs(V):
#     q = deque()
#     q.append(V)       
#     BFS_visit[V] = True
#     while q:
#         V = q.popleft()
#         print(V, end = " ")
#         for i in range(1, N + 1):
#             if BFS_visit[i] == False and graph[V][i] == 1:
#                 q.append(i)
#                 BFS_visit[i] = True


# dfs(V)
# bfs(V)


from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)