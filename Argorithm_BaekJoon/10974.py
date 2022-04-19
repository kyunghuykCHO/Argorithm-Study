import itertools

n = int(input())
list1 = []
for i in range(n):
    list1.append(str(i+1))

list2 = itertools.permutations(list1)
for i in list2:
    for j in i:
        print(j,end=' ')
    print()