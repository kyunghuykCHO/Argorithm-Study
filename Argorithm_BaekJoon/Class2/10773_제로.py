K = int(input())
numberstack = []
for i in range(K):
    num = int(input())
    if num==0 :
        numberstack.pop()
    else :
        numberstack.append(num)
print(sum(numberstack))