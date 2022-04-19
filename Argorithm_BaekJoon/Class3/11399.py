N = int(input())
P = list(map(int,input().split()))
P.sort()
tmp = 0
for i in range(len(P)):
    tmp += P[i]
    P[i] = tmp
print(sum(P))