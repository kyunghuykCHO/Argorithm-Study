import sys
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))

left,right = 0,max(trees)
while left<=right:
    mid = (left+right)//2
    height = 0
    for i in trees:
        if i>=mid :
            height += (i-mid)
    if height >= M:
        left = mid+1
    else:
        right = mid-1

print(right)