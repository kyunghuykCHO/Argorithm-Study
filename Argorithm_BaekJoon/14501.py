# OutDate = int(input())
# periodList = []
# priceList = []
# totalList=[]

# for i in range(OutDate):
#     period, price = map(int,input().split())
#     periodList.append(period)
#     priceList.append(price)

# index = len(periodList)-1

# # for i in range(index):
# #     startpoint=0
# #     price=0
# #     if(i+periodList[i]<=index):
# #         startpoint+=periodList[i]
# #         price+=priceList[i]
# #         for j in range(startpoint,index):
# #             if(j+periodList[j]<=index):
# #                 startpoint+=periodList[j]
# #                 price+=priceList[j]



n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])