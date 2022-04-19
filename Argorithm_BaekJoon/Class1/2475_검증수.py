cerial = list(map(int,input().split()))
for i in range(len(cerial)):
    cerial[i]=cerial[i]*cerial[i]
print(sum(cerial)%10)
