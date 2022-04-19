numberlist = []
for i in range(9):
    numberlist.append(int(input()))
print(max(numberlist))
print(numberlist.index(max(numberlist))+1)