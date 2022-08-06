s = "12223"
lst = list(s)
dp = [0 for i in range(len(lst))]
for i in range(2,len(lst)):
    if lst[i-2] == lst[i-1] == lst[i]:
        dp[i] = (int(lst[i]))
temp = max(dp)
answer = temp*100 + temp*10 + temp
print(answer)
