import sys

bag, n = map(int,input().split())
gems = []
answer = 0
for i in range(n):
    gem, price = map(int,input().split())
    gems.append((gem,price))
gems.sort(key=lambda x: (x[1]), reverse = True)
for gem in gems:
    if gem[0] >= bag :
        answer += bag*gem[1]
        break
    elif bag == 0 :
        break
    elif gem[0] < bag :
        answer += gem[0]*gem[1]
        bag = bag-gem[0]
print(answer)