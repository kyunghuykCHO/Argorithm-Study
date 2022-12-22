K,N = map(int,input().split())
lList = []
for i in range(K):
    lList.append(int(input()))
left, right = 1,max(lList) # left starts 1 not 0 , max(lList) -> 구하는 것 = 최대 길이..! 

while left<=right:
    mid = (left+right)//2
    answer = 0
    for l in lList:
        answer += l//mid
    if answer < N: 
        right = mid-1
    else:
        left = mid+1
        
    
print(right) # print(right) MAX ? or MIN ? 