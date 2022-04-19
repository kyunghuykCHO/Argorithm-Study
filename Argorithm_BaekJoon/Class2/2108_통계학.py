# N = int(input())
# numberlist = []
# for i in range(N):
#     numberlist.append(int(input()))
# print(round(sum(numberlist)//len(numberlist)))
# numberlist.sort()
# idx = len(numberlist)//2
# print(numberlist[idx])
# high_count = []
# for j in numberlist:
#     n = numberlist.count(j)
#     high_count.append((j,n))
# high_count = list(set(high_count))
# high_count.sort(key = lambda x:(-x[1],x[0]))
# if len(high_count)>=2 :
#     if high_count[0][1] == high_count[1][1]:
#         result = high_count[1][0]
#     else :
#         result = high_count[0][0]
# elif len(high_count)==1 :
#     result = high_count[0][0]
# print(result)
# print(max(numberlist)-min(numberlist))


import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_s = Counter(nums).most_common()
print(round(sum(nums) / n))
print(nums[n // 2])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(nums[-1] - nums[0])