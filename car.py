K,M = map(int, input().split())
Klist = list(map(int,input().split()))
Mlist=[]
for i in range(M):
    Mlist.append(list(map(int,input().split())))

Result = []
for car in Mlist:
    if car[0]-car[1] >=0:
        startPoint = car[0]-car[1]
    else:
        startPoint = 0
    endPoint = car[0]+car[1]
    count = 0
    for oil in Klist:
        if startPoint <= oil <= endPoint:
            count += 1
    Result.append(count)
            
for res in Result:
    print(res)