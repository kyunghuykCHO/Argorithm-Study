N = int(input())
ans = N
for i in range(1,N):
    result = i
    result += sum(map(int,str(i)))
    if result == N and i < ans:
        ans = i
if(ans == N):
    print(0)
else:
    print(ans)

