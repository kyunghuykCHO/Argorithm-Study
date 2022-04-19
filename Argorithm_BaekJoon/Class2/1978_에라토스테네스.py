import math

N = int(input())
numberlist = list(map(int,input().split()))

def find_primeNumber(arr):
    primenumbers = 0
    for num in arr:
        cnt = 0
        if num==1:
            cnt+=1
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0 :
                cnt+=1
        if cnt==0 :
            primenumbers+=1
    return primenumbers

print(find_primeNumber(numberlist))