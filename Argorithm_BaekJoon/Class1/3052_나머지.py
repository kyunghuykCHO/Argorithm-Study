nset = set()
for i in range(10):
    a = int(input())
    b = a%42
    nset.add(b)
print(len(nset))