# def getSmallIndex(distance,visited):
#     minvalue = INF
#     idx = 0
#     for i in range(n):
#         if(distance[i] < minvalue and visited[i]==False):
#             minvalue = distance[i]
#             idx = i
#     return idx

# def dijkstra(start):
#     visited = [False]*n
#     distance = [INF]*n
#     for i in range(n):
#         distance[i] = m[start][i]
#     visited[start] = False
#     for i in range(n-1):
#         current = getSmallIndex(distance,visited)
#         visited[current] = True
#         for j in range(n):
#             if distance[current]+m[current][j] < distance[j]:
#                 distance[j] = distance[j] + m[current][j]
#     res.append(distance)

# n,e= map(int,input().split())
# INF = 99999
# m = [[INF]*n for i in range(n)]
# for i in range(e):
#     a,b,c = map(int,input().split())
#     m[a-1][b-1] = m[b-1][a-1] = c
# v1,v2 = map(int,input().split())
# v1 -= 1 
# v2 -= 1
# res = []
# dijkstra(0)
# dijkstra(v1)
# dijkstra(v2)
# result = min(res[0][v1]+res[1][v2]+res[2][n-1], res[0][v2]+res[2][v1]+res[1][n-1])
# if result > INF:
#     print(-1)
# else:
#     print(result)


from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, e = map(int, input().split())
s = [[] for i in range(n + 1)]
inf = sys.maxsize
for i in range(e):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
v1, v2 = map(int, input().split())
def dijkstra(start):
    dp = [inf for i in range(n + 1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, c = heappop(heap)
        for n_n, n_w in s[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heappush(heap, [wei, n_n])
    return dp
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < inf else -1)