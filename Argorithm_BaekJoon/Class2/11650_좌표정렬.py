N = int(input())
field = []
for i in range(N):
    x,y = map(int,input().split())
    field.append((x,y))

field = sorted(field)

for j in field:
    print(j[0], j[1])