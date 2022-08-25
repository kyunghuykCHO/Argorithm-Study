import sys 
import heapq
input = sys.stdin.readlines

# 산봉우리는 1개만 , 출입구는 처음과 끝 only , intensity 를 최소화합니다. 
# gates 배열로부터 출발지를 불러옵니다 
# 각각의 gate 를 출발지로 결정하고 summits 까지 도달하는 경로 중 가장 작은 intensity 를 결정합니다 

def dijkstra(n, gate, mountain, distance,summits):
    intensities = [0 for i in range(n+1)]
    intense = 0
    hq = []
    heapq.heappush(hq, (0,gate))
    distance[gate] = 0
    while hq:
        dist,now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for i in mountain[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))
                if i[0] not in summits:
                    intense = max(intense, i[1])
                else:
                    intensities[i[0]] = intense
    max_intensity = 0
    res_summit = 0
    for summit in summits:
        if intensities[summit]> max_intensity:
            res_summit = summit 
            max_intensity = intensities[summit]
    return res_summit,max_intensity



def solution(n, paths, gates, summits):
    INF = int(1e9)
    answer = []
    mountain = [[] for _ in range(n+1)]
    intensity = INF
    summit = INF
    for path in paths:
        mountain[path[0]].append((path[1],path[2]))
        mountain[path[1]].append((path[0],path[2]))

    for gate in gates:
        distance = [INF for _ in range(n+1)]
        res_summit, res_intensity = dijkstra(n, gate,mountain,distance,summits)
        if res_intensity<intensity :
            intensity = res_intensity
            summit = res_summit 
    answer=[summit,intensity]
    return answer


print(solution(6,[[1,2,3],[2,3,5],[2,4,2],[2,5,4],[3,4,4],[4,5,3],[4,6,1],[5,6,1]],[1,3],[5]))
print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2, 3, 4]))