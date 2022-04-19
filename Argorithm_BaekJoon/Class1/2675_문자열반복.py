T = int(input())
for i in range(T):
    count, string = map(str, input().split())
    count = int(count)
    for j in string:
        for k in range(count):
            print(j,end="")
    print()