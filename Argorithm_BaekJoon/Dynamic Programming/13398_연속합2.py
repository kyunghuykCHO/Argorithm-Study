# n = int(input())
# arr = list(map(int,input().split()))
# dp = [-1000] * len(arr)
# dp[0] = arr[0]
# maxValue = -1000

# for i in range(1,len(arr)):
#     for j in range(1,len(arr)):
#         if i==j:
#             continue
#         elif j==i+1:
#             dp[j] = max(arr[j],dp[j-2]+arr[j])
#             maxValue = max(maxValue,dp[j])
#         else:
#             dp[j] = max(arr[j],dp[j-1]+arr[j])
#             maxValue = max(maxValue,dp[j])
#     dp = [-1000] * len(arr)
#     dp[0] = arr[0]    
# print(max(maxValue,sum(arr)))




# ===================================================================================




n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]
dp[0][0] = arr[0] 
if n > 1:
    answer = -1000000
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i-1] + arr[i])
        answer = max(answer, dp[0][i], dp[1][i])
    print(answer)
else:
    print(dp[0][0])