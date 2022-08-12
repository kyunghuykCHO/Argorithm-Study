from collections import deque
def bfs(place):
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1] 
    P = []
    for i in range(5): 
        for j in range(5):
            if place[i][j] == 'P':
                P.append((i, j))
    for point in P:
        dq = deque()
        dq.append(point)
        visit = [[0]*5 for i in range(5)] 
        distance = [[0]*5 for i in range(5)] 
        while dq:
            y, x = dq.popleft()
            visit[y][x] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visit[ny][nx] == 0:
                    if place[ny][nx] == 'O':
                        dq.append((ny, nx))
                        visit[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for i in places:
        place = []
        for lst in i:
            place.append(list(lst))
        answer.append(bfs(place))
    print(answer)
    return answer

solution([["POOOP", "OXXOX", "OXXPX", "OPXOX", "PXXXP"]])
