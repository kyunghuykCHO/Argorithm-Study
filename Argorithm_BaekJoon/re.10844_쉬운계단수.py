# from collections import deque 

# N = int(input())
# dq = deque([])

# for i in range(1,11):
#     dq.append(i)
# cnt = 1
# result = 0

# while cnt<N:
#     a = dq.popleft()
#     if 1<=a<9 :
#         b = a-1
#         dq.append(b)
#         c = a+1
#         dq.append(c)
#         result +=2
#     if a==0 :
#         b = a+1
#         dq.append(b)
#         result+=1
#     if a==9 :
#         b = a-1
#         dq.append(b)
#         result+=1
#     if a==10 :
#         dq.append(10)
#         cnt+=1

# if N==1:
#     print(9)
# else:
#     print(result)

n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)