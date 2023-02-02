from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(r,c,maps):
    global v
    dq = deque([])
    count = 0
    dq.append((r,c))
    v[r][c] = True
    while dq:
        r,c = dq.popleft()
        # if v[r][c] == True :
        #     continue
        count += int(maps[r][c])
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) and maps[nr][nc] != "X" and v[nr][nc] == False:
                dq.append((nr,nc))
                v[nr][nc] = True # 버릇적으로 여기다가 Visit 걸어랑 ㅋㅋ 
    return count

def solution(maps):
    global v
    answer = []
    v = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and v[i][j] == False:
                answer.append(bfs(i,j,maps))
    if len(answer) == 0 :
        return [-1]
    answer.sort()
    return answer


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))