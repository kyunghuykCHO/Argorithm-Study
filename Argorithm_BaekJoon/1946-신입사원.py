import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    rank = [[0,0] for _ in range(N)]
    for j in range(N):
        a,b = map(int,input().split())
        rank[j][0]=a
        rank[j][1]=b
    rank.sort(key=lambda x:x[0])

    count=1
    m = rank[0][1]
    for k in range(1, len(rank)):
        if rank[k][1] < m :
            count+=1
            m = rank[k][1]

    print(count)


# 정렬필요 x --> 입력 받을 때 인덱스로 바로 
# 면접순위 1 일시 break
# 효율 ?? 튜플. 