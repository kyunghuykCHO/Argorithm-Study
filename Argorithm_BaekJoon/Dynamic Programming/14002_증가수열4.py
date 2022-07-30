# N = int(input())
# A = list(map(int, input().split()))
# dp = [1] * N
# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i],dp[j]+1)
# R=[]
# s = max(dp)
# for i in range(N-1,-1,-1):
#     if dp[i] == s:
#         R.append(A[i])
#         s-=1

# R.reverse()
# print(max(dp))
# for i in R:
#     print(i,end=' ')
    
    
    
N = int(input())
L = list(map(int,input().split()))
dp = [(1,L[i]) for i in range(N)]
for i in range(N):
    for j in range(i):
        if L[j] < L[i]:
            if dp[i][0] < dp[j][0] + 1:
                tmp = []
                tmp.append(dp[j][0]+1)
                for k in range(1,len(dp[j])):
                    tmp.append(dp[j][k])
                tmp.append(L[i])
                dp[i] = tuple(tmp)
tmpdp = max(dp)
print(tmpdp[0])
print(*tmpdp[1:])