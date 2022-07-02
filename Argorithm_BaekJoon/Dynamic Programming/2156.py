n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
dp = []
if n == 1:
    print(w[0])
elif n == 2:
    print(w[0]+w[1])
elif n == 3:
    print(max(w[0]+w[1], w[0]+w[2], w[1]+w[2]))
else:
    dp.append(w[0])
    dp.append(w[0]+w[1])
    dp.append(max(w[0]+w[1], w[0]+w[2], w[1]+w[2]))
    for i in range(3, n):
        dp.append(max(dp[i-1], dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i]))
    print(dp[n-1])
    
