a,b = map(int,input().split())
result1 = max(a,b)
for i in range(1,result1+1):
    if a%i==0 and b%i==0 :
        result1 = i
small = min(a,b)
big = max(a,b)
cnt = 1
while True:
    if (big*cnt)%small == 0 :
        result2 = (big*cnt)
        break
    else :
        cnt+=1
print(result1)
print(result2)