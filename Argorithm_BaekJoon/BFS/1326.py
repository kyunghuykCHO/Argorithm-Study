from collections import deque

N = int(input())
stones = list(map(int,input().split()))
departure, destination = map(int,input().split())
if N==1:
    print(0)
else:
    steppingStone = [[0,0,0] for i in range(N+1)]
    visit = [False] * (N+1)
    visit[0] = True
    for i, stone in enumerate(stones):
        steppingStone[i+1][0] = stone
        steppingStone[i+1][1] = 0
        steppingStone[i+1][2] = i+1
    dq = deque()
    cnt = 0
    dq.append((steppingStone[departure], cnt))
    while dq:
        stone, cnt = dq.popleft()
        visit[stone[2]] = True
        stone[1] += 1
        if stone[2] == destination:
            break         
        multiple = 1
        while stone[2]-stone[0]*multiple >=0 or stone[2]+stone[0]*multiple <=N :
            if stone[2]+stone[0]*multiple <=N and visit[stone[2]+stone[0]*multiple] == False :
                dq.append((steppingStone[stone[2]+stone[0]*multiple], cnt+1))
            if stone[2]-stone[0]*multiple >=0 and visit[stone[2]-stone[0]*multiple] == False:
                dq.append((steppingStone[stone[2]-stone[0]*multiple], cnt+1))
            multiple+=1
            
    if visit[destination]==False:
        print(-1)
    else :
        print(cnt)


