N = int(input())
field= []
for i in range(N):
    x,y = map(int,input().split())
    field.append((x,y))

field.sort(key = lambda x: (x[1],x[0]))

for j in field:
    print(j[0], j[1])