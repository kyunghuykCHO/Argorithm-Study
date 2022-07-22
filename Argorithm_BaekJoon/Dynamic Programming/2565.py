# def check(cables):
#     a = cables[0][1]
#     for i in range(1,len(cables)):
#         b = cables[i][1]
#         if b<a:
#             return 1
#         else:
#             a = b
#     return 0

# n = int(input())
# cables = []
# for i in range(n):
#     a,b = map(int,input().split())
#     cables.append([a,b])
# # print(cables)
# cables.sort(key=lambda x:x[0])
# # print(cables)
# stop = 1
# answer = 0

# while True :
#     if check(cables)==0:
#         break
#     gap = 0
#     idx = 0
#     for i in range(n):
#         if abs(cables[i][1]-cables[i][0])>gap:
#             gap = abs(cables[i][1]-cables[i][0])
#             idx = i
#     cables[idx][0]=0
#     cables[idx][1]=0
#     cables.sort(key=lambda x:x[0])
#     answer+=1
# print(answer)

    
    
n = int(input())
w = []
w_b = []
dp = [0 for i in range(n)]
for i in range(n):
    w.append(list(map(int, input().split())))
w.sort(key = lambda x:x[0])
for i in range(n):
    w_b.append(w[i][1])
for i in range(n):
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))
