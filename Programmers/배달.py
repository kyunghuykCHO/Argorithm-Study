import heapq
import math

def dijkstra(start,graph,distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q)
        # print("dist = {} and now = {}".format(dist,now))
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        # print("========== distance =========")
        # print(distance)
    return distance

#마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.
def solution(N, road, K):
    INF = math.inf 
    answer = 0
    graph = [[] for _ in range(N+1)]
    for node in road:
        graph[node[1]].append((node[0],node[2]))
        graph[node[0]].append((node[1],node[2]))
    distance = [INF for _ in range(N+1)]
    start = 1
    distance = dijkstra(start,graph,distance)
    # print("========= result =========")
    # print(graph)
    # print(distance)
    for i in distance:
        if i<=K:
            answer +=1
    print(answer)
    return answer



solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)