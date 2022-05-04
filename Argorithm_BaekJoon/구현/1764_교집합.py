n,m = map(int,input().split())
listen = set()
for i in range(n):
    listen.add(input())
look = set()
for j in range(m):
    look.add(input())
result = sorted(list(listen&look))
print(len(result))
for k in result:
    print(k)    