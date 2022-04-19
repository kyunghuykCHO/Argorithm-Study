N = int(input())
graph = [[0 for i in range(N)] for j in range(N)]
visit=[False for _ in range(N)]
for k in range(N):
    graph[k] = list(map(int, input().split()))

result = 0
def dfs(V, result):
    visit[V] = True
    if visit.count(True)==N:
        print(result,end=" ")
    for i in range(N):
        if visit[i]==False and graph[V][i]!=0:
            result += graph[V][i]
            dfs(i)

