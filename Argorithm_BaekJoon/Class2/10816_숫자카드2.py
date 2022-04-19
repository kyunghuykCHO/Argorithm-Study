# def binary_search(target,arr,cnt):
#     start = 0
#     end = len(arr)-1
#     while start <= end:
#         mid = (start+end)//2
#         if arr[mid]==target:
#             cnt+=1
#             del arr[mid]
#             return binary_search(target,arr,cnt)
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
#     return cnt

# N = int(input())
# card = list(map(int,input().split()))
# card.sort()
# M = int(input())
# search = list(map(int,input().split()))
# for i in search:
#     cnt=0
#     print(binary_search(i,card,cnt),end=" ")

from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

count = Counter(card)

for i in range(len(test)):
    if test[i] in count:
        print(count[test[i]], end=' ')
    else:
        print(0, end=' ')