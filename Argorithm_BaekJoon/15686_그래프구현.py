from itertools import combinations

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))
result = 99999
house = []   
chicken = []     

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append([i, j])
        elif maps[i][j] == 2:
            chicken.append([i, j])

for chick in combinations(chicken, m):
    distance = 0
    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chick[j][0]) + abs(h[1] - chick[j][1]))
        distance += chi_len
    result = min(result, distance)

print(result)