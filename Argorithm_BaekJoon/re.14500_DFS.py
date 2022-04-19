# from collections import deque

# N,M = map(int,input().split())
# F = []
# for i in range(N):
#     F.append(list(map(int,input().split())))
# result = 0

# def bfs(a,b,visit,tmplist):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     q = deque()
#     q.append((a,b))
#     visit[a][b]=False
#     while q:
#         a,b= q.popleft()
#         for i in range(4):
#             tx = b + dx[i]
#             ty = a + dy[i]
#             if 0<=tx<len(tmplist[0]) and 0<=ty<len(tmplist) and visit[ty][tx]==True:
#                 q.append((ty,tx))
#                 visit[ty][tx]=False
#     return 1

# def sumLine(list2):
#     sum = 0
#     for line in list2:
#         for E in line:
#             sum+=E
#     return sum

# def makevisit(list3):
#     row = len(list3)
#     col = len(list3[0])
#     visit = [[False]*col for _ in range(row)]
#     return visit

# def sumLine2(list2):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     row = len(list2)
#     col = len(list2[0])
#     reslist = []
#     q = deque([])
#     for a in range(len(list2)):
#         for b in range(len(list2[0])):
#             visit = makevisit(list2)
#             res = list2[a][b]
#             q.append((a,b,1,res))
#             visit[a][b]=True
#             while q:
#                 a,b,count,res = q.popleft()
#                 if count==3:
#                     reslist.append(res)
#                     break
#                 for i in range(4):
#                     tx = b + dx[i]
#                     ty = a + dy[i]
#                     if 0<=tx<col and 0<=ty<row and visit[ty][tx]==False:
#                         res += list2[ty][tx]
#                         q.append((ty,tx,count+1,res))
#                         visit[ty][tx]=True        
#     return max(reslist)
            
# def squareSearch(F,col,row):
#     global result
#     for i in range(len(F)-row+1):
#         for j in range(len(F[0])-col+1):
#             sum = sumLine([m[j:j+col] for m in F[i:i+row]])
#             if sum > result :
#                 result = sum

# def squareSearch2(F,col,row):
#     global result
#     for i in range(len(F)-row+1):
#         for j in range(len(F[0])-col+1):
#             sum = sumLine2([m[j:j+col] for m in F[i:i+row]])
#             if sum > result :
#                 result = sum

# squareSearch(F,2,2)
# squareSearch(F,1,4)
# squareSearch(F,4,1)
# squareSearch2(F,2,3)
# squareSearch2(F,3,2)
# print(result)

import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# INPUT
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)