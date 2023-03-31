import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) 

# N : 마을 수, M : 단방향 도로 수, X : 목표 마을 번호 
N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    startNode, endNode, weight = map(int,input().split())
    graph[startNode].append((endNode,weight))

# 다익스트라 함수
def dijkstra(start):
    # 다익스트라 여러번 호출될듯.. Distance 배열을 지역변수로 선언
    distance = [INF] * (N+1)
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    while hq:
        currentDist, currentNode = heapq.heappop(hq)
        # 이미 방문지역일시 통과
        if distance[currentNode] < currentDist:
            continue
        # 인접 노드 탐색 
        for connectedNode in graph[currentNode]:
            cost = currentDist + connectedNode[1]
            # 최소 거리가 계산된다면 우선순위 큐 push 
            if cost < distance[connectedNode[0]]:
                distance[connectedNode[0]] = cost
                heapq.heappush(hq, (cost, connectedNode[0]))
    return distance

students = [0] * (N+1)
for i in range(1, N+1):
    distanceToGoList = dijkstra(i)
    distanceToX = distanceToGoList[X]
    distanceToComeList = dijkstra(X)
    distanceToHome = distanceToComeList[i]
    roundTripDistance = distanceToX + distanceToHome
    students[i] = roundTripDistance
print(max(students))