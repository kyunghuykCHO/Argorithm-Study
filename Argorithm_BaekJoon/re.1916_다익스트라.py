cities = int(input())
NumberofBus = int(input())
INF = 100000
B = [[INF]*cities for _ in range(cities)]
for i in range(NumberofBus):
    r,c,w = map(int,input().split())
    B[r-1][c-1] = w
# 2차원 그래프로 가중치값 설정

S,E = map(int,input().split())
S,E = S-1,E-1
# 출발지점 도착지점 입력

def getSmallIndex(D,V):
    minn = INF
    idx = 0
    for i in range(cities):
        if(D[i]<minn and not V[i]):
            minn = D[i]
            idx = i
    return idx
#방문하지 않은 노드 중 가장 최소 가중치를 갖는 index 값 return 함수

V = [False]*cities
# VISIT 배열 생성

def dijkstra(S):
    D = B[S]
    V[S] = True
    for i in range(cities-1):
        # 출발지점을 뺀 나머지 노드 check
        current = getSmallIndex(D,V)
        # 가장 작은 가중치 idx 가져옴
        V[current] = True
        for j in range(cities):
            if not V[j] :
                if D[current] + B[current][j] < D[j] :
                    D[j] = D[current] + B[current][j]
                    # 경로 최신화 --> 최신화되면서 경로까지 저장 됨
    return D
# 다익스트라 알고리즘 

D = dijkstra(S)
print(D[E])