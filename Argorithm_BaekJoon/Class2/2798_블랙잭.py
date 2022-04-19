N,M = map(int,input().split())
cardlist = list(map(int,input().split()))
gap = M
tmp = 0
for a in range(0,N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            tmp = cardlist[a]+cardlist[b]+cardlist[c]
            if M-tmp < gap and tmp <= M :
                gap = M-tmp
                result = tmp
print(result)