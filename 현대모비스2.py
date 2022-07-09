from queue import PriorityQueue
que = PriorityQueue()
M,N = map(int,input().split())
m = [[0]*N for i in range(N)]
for i in range(N):
    s,t,a,b,c = map(int, input().split())
    m[s-1][t-1] = m[t-1][s-1] = (a,b,c)

# 1번 지구 -> 주택지구 
# 2번 지구 -> 산업지구 
# 다익스트라 -> 우선순위 큐 