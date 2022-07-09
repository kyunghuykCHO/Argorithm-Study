# n = int(input())
# box = []
# dp = [0 for i in range(n)]
# box = list(map(int,input().split()))
# dp[0] = 1
# for i in range(1,n):
#     maxSize = box[i]
#     cnt = 1
#     for j in range(i,-1,-1):
#         if box[j]<maxSize:
#             cnt+=1
#             maxSize = box[j]
#     dp[i] = max(dp[i-1],cnt)
# print(dp)
# if n==1:
#     print(1)
# else:
#     print(dp[-1])



# from collections import deque
# n = int(input())
# box = []
# dp = [0 for i in range(n)]
# box = list(map(int,input().split()))
# dq = deque()
# dq.append((1,box[0]))
# dp[0] = 1
# for i in range(1,n):
#     count , size = dq.popleft()
#     if box[i]>size:
#         dq.append((count+1,box[i]))
#         dp[i] = dp[i-1]+1
#     else:
#         dp[i] = dp[i-1]
# print(dp)



n = int(input())
box = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = 1
for i in range(1, n):
    check = 1
    for j in range(i):
        if box[i] > box[j]:
            check = max(check, dp[j]+1)
    dp[i] = check
print(max(dp))