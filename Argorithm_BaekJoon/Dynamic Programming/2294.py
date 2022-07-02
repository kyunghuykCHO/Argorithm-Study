n, k = map(int,input().split())
c =[]
for i in range(n):
   c.append(int(input()))
dp = [100000] * (k+1)
dp[0] = 0
for i in c:
   for j in range(i, k+1):
       dp[j] = min(dp[j],dp[j-i]+1)
if dp[k]==100000:
    print(-1)
else:
    print(dp[k])