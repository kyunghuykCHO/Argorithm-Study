t, w = map(int, input().split())

dp = [0] * (t+1)
plum = [0]

for i in range(t):
    plum.append(int(input()))
for i in range(w+1):
    for j in range(1, t+1):
        if i%2==0:
            if plum[j]==1:
                dp[j] = max(dp[j]+1, dp[j-1]+1)
            elif plum[j]==2:
                dp[j] = max(dp[j], dp[j-1])
        elif i%2==1:
            if plum[j]==1:
                dp[j] = max(dp[j], dp[j-1])
            elif plum[j]==2:
                dp[j] = max(dp[j]+1, dp[j-1]+1)
print(dp[-1])
    
'''
every index of zero initialize 'zero'
PLUM  2 1 1 2 2 1 1 
DP    0 0 0 0 0 0 0
i=0 (w=0) 일 때 --> 현재 Tree의 위치는 1번 
DP    0 1 2 2 2 3 4 
i=1 (w=1) 일 때 --> 현재 Tree의 위치는 2번 
DP    1 1 2 3 4 4 4 
i=2 (w=2) 일 때 --> 현재 Tree의 위치는 1번 
DP    1 2 2 3 4 5 6

'''