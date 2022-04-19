# TestCase = int(input())
# for i in range(TestCase):
#     n = int(input())
#     stickers = [[0]*n for j in range(2)]
#     stickers[0] = list(map(int,input().split()))
#     stickers[1] = list(map(int,input().split()))
#     # 입력
    
#     visit = [[0]*n for k in range(2)]
#     # visit 함수

#     result = 0
#     while True:
#         if visit[0].count(1) + visit[1].count(1) == 2*n :
#             break
#         maximum = 0
#         for l in range(2):
#             for m in range(n):
#                 if stickers[l][m] >= maximum and visit[l][m]==0 :
#                     maximum = stickers[l][m]
#                     a = l
#                     b = m
#         result += stickers[a][b]
#         visit [a][b] = 1
#         if a==0:
#             visit[a+1][b] = 1
#             if b==0:
#                 visit[a][b+1] = 1
#             elif b==n-1:
#                 visit[a][b-1]=1
#             else:
#                 visit[a][b-1]=1
#                 visit[a][b+1]=1
#         elif a==1:
#             visit[a-1][b] = 1
#             if b==0:
#                 visit[a][b+1] = 1
#             elif b==n-1:
#                 visit[a][b-1]=1
#             else:
#                 visit[a][b-1]=1
#                 visit[a][b+1]=1
#     print(result)
            

TestCase = int(input())
for i in range(TestCase):
    n = int(input())
    stickers = [[0]*n for j in range(2)]
    stickers[0] = list(map(int,input().split()))
    stickers[1] = list(map(int,input().split()))
    for k in range(1, n):
        if k == 1:
            stickers[0][k] += stickers[1][k - 1]
            stickers[1][k] += stickers[0][k - 1]
        else:
            stickers[0][k] += max(stickers[1][k - 1], stickers[1][k - 2])
            stickers[1][k] += max(stickers[0][k - 1], stickers[0][k - 2])
    print(max(stickers[0][n - 1], stickers[1][n - 1]))
