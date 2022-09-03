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
        if now in summits or intensity > visit[now]:
            continue
        for next_intensity, next in graph[now]:
            max_intensity = max(intensity, next_intensity)
            if max_intensity < visit[next]:
                visit[next] = max_intensity
                heapq.heappush(hq, (max_intensity, next))
    result = [0, 10000001]
    for summit in summits:
        if visit[summit] < result[1]:
            result[0] = summit
            result[1] = visit[summit]

    return result
        
        
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for path in paths:
        graph[path[0]].append((path[2], path[1]))
        graph[path[1]].append((path[2], path[0]))
    summits.sort()
    answer = (searching(n,gates,summits,graph))
    return answer