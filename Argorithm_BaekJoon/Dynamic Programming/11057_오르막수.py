# N = int(input())
# dp = []
# result = [0 for i in range(N)]
# result[0] = 1000
# for i in range(10):
#     dp.append(i+1)
# dp.reverse()
# for _ in range(N-1):
#     for i in range(len(dp)):
#         sum = 0
#         for j in range(i,10):
#             sum += dp[j]
#         dp[i] = sum
# print(dp[0]%10007)

n = int(input())

dp = [1] * 10

for _ in range(1, n):
    for i in range(10):
        dp[i] = sum(dp[i:])

print(sum(dp)%10007)


