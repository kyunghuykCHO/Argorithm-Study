import heapq 
import sys
input = sys.stdin.readlines
INF = int(1e9)

def searching(n,gates,summits,graph):
    hq = []  
    visit = [INF] * (n + 1)
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        visit[gate] = 0
    while hq:
        intensity, now = heapq.heappop(hq)
        if now in summits:
            return [now, intensity]  
        for next_intensity, next in graph[now]:
            max_intensity = max(intensity, next_intensity)
            if max_intensity < visit[next]:
                visit[next] = max_intensity
                heapq.heappush(hq, (max_intensity, next))

    return [-1, -1]
    
def solution(n, paths, gates, summits):
    res = []
    graph = [[] for _ in range(n+1)]
    for path in paths:
        graph[path[0]].append((path[2], path[1]))
        graph[path[1]].append((path[2], path[0]))
    res.append(searching(n,gates,summits,graph))
    res.sort(key = lambda x : (x[1],x[0]))
    answer = res[0]
    return answer