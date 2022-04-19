import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {}

for _ in range(N):
    site, ps = input().split()
    memo[site] = ps

for _ in range(M):
    print(memo[input().rstrip()])