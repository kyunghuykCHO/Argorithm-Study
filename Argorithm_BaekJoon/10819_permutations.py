from itertools import permutations
N = int(input())
Nlist = list(map(int,input().split()))
a = list(permutations(Nlist, N))
result = 0
for i in a:
    tmp = 0
    for j in range(N-1):
        tmp += abs(i[j]-i[j+1])
    if tmp > result:
        result = tmp
print(result)