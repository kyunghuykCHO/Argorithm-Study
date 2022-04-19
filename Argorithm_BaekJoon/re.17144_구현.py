# R,C,T = map(int,input().split())
# F = []
# for _ in range(R):
#     F.append(list(map(int,input().split())))

# def diff(x,y,copy_value):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     cnt = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < R and 0 <= ny < C and F[nx][ny] != -1:
#             F[nx][ny] += copy_value//5
#             cnt+=1
#     F[x][y] -= (copy_value//5)*cnt

# def anticlockwise(x,y):
#     tmp = F[x][y]
#     F[x][y] = 0
#     while True:
#         y+=1
#         if y>=C:
#             y-=1
#             break
#         tmp2 = F[x][y]
#         F[x][y] = tmp
#         tmp = tmp2
#     if x-1 <0 :
#         return
#     for j in range(x):
#         x-=1
#         tmp2 = F[x][y]
#         F[x][y] = tmp
#         tmp = tmp2
#     for k in range(C-1):
#         y-=1
#         tmp2 = F[x][y]
#         F[x][y] = tmp
#         tmp = tmp2
#     for l in range(x-1):
#         x+=1
#         tmp2 = F[x][y]
#         F[x][y] = tmp
#         tmp = tmp2
        

# def clockwise(x,y):
#     tmpp = F[x][y]
#     F[x][y] = 0
#     while True:
#         y+=1
#         if y>=C:
#             y-=1
#             break
#         tmp3 = F[x][y]
#         F[x][y] = tmpp
#         tmpp = tmp3
#     if x+1 > R-1:
#         return
#     for j in range(R-x-1):
#         x+=1
#         tmp3 = F[x][y]
#         F[x][y] = tmpp
#         tmpp = tmp3
#     for k in range(C-1):
#         y-=1
#         tmp3 = F[x][y]
#         F[x][y] = tmpp
#         tmpp = tmp3
#     while True:
#         x-=1
#         if F[x][y] == -1:
#             break
#         tmp3 = F[x][y]
#         F[x][y] = tmpp
#         tmpp = tmp3


# for j in range(T):
#     vac = 0
#     F_copy = []
#     for line in F:
#         F_copy.append(line.copy())
#     for i in range(len(F)):
#         for j in range(len(F[0])):
#             if F_copy[i][j] !=-1 and F_copy[i][j]>0:
#                 diff(i,j,F_copy[i][j])
#     if len(F[0]) == 1:
#         res = 0
#         for _ in F:
#             res+=sum(_)
#         print(res+2)
#         exit()
#     for q in range(R):
#         if F[q][0] == -1 :
#             vac+=1
#         if vac == 1:
#             anticlockwise(q,1)
#         if vac == 2:
#             clockwise(q,1)
#             break
# result = 0
# for line in F:
#     result += sum(line)
# print(result+2)

## 먼지 퍼뜨리기
def spread():
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]                        # 서, 동, 북, 남 방향
                    if not(0<=nx<r and 0<=ny<c): continue            # 범위를 벗어난다면.
                    if board[x][y] < 5: continue                     # 5보다 작다면 먼지가 퍼지지 않는다.
                    if (nx, ny) == (air_cleaner[0], 0): continue
                    if (nx, ny) == (air_cleaner[1], 0): continue
                    cnt = cnt + 1                                    # cnt 증가
                    board2[nx][ny] = board2[nx][ny] + board[x][y]//5 # board2에 퍼진 먼지량 추가
                board2[x][y] = board2[x][y] + board[x][y] - board[x][y]//5*cnt
 
 
def clean():
    ## 윗부분 반시계방향
    for i in range(air_cleaner[0]-2, -1, -1):
        board2[i+1][0] = board2[i][0]
    for i in range(1, c):
        board2[0][i-1] = board2[0][i]
    for i in range(1, air_cleaner[0]+1):
        board2[i-1][-1] = board2[i][-1]
    for i in range(c-2, 0, -1):
        board2[air_cleaner[0]][i+1] = board2[air_cleaner[0]][i]
    board2[air_cleaner[0]][1] = 0
    ## 아랫부분 시계방향
    for i in range(air_cleaner[1]+2, r):
        board2[i-1][0] = board2[i][0]
    for i in range(1, c):
        board2[-1][i-1] = board2[-1][i]
    for i in range(r-2, air_cleaner[1]-1, -1):
        board2[i+1][-1] = board2[i][-1]
    for i in range(c-2, 0, -1):
        board2[air_cleaner[1]][i+1] = board2[air_cleaner[1]][i]
    board2[air_cleaner[1]][1] = 0
 
 
if __name__ == '__main__':
    ## 행(r), 열(c), 시간(t)
    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    # 공기 청정기 행 위치
    air_cleaner = []
    for i in range(r):
        if board[i][0] == -1: air_cleaner.append(i)
    # 서 동 북 남
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    # 1번 시행
    board2 = [[0]*c for _ in range(r)]
    spread()
    clean()
    ## t-1번 시행
    for time in range(t-1):
        board = board2.copy()
        board2 = [[0]*c for _ in range(r)]
        spread()
        clean()
    ## 전체 총합 구하기
    sumv = 0
    for i in range(r):
        for j in range(c):
            if board2[i][j] > 0: sumv = sumv + board2[i][j]
    print(sumv)
