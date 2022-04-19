V,E = map(int,input().split())
K = int(input())
M = [[0]*V for _ in range(V)]
for i in range(E):
    a,b,w = map(int,input().split())
    M[a-1][b-1] = w
D = [10000]*V