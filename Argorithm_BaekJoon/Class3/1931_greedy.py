N = int(input())
a = []
for i in range(N):
    a.append(list(map(int,input().split())))
a.sort(key = lambda x: (x[1],x[0]))
time = a[0][1]
result = 1
for i in range(1,len(a)):
    if a[i][0]>=time:
        time = a[i][1]
        result+=1
print(result)