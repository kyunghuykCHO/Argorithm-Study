n = int(input())
for i in range(n):
    if i == 0 :
        top = int(input())
    elif i == 1 :
        tmpList1 = list(map(int,input().split()))
        for j in range(len(tmpList1)):
            tmpList1[j] += top
    else :
        tmpList2 = list(map(int,input().split()))
        for j in range(len(tmpList2)):
            if j == 0 :
                tmpList2[j] += tmpList1[j]
            elif 1<=j<=len(tmpList2)-2 :
                tmpList2[j] += max(tmpList1[j-1], tmpList1[j])
            elif j == len(tmpList2)-1 :
                tmpList2[j] += tmpList1[j-1]
        tmpList1 = []
        for tmp in tmpList2:
            tmpList1.append(tmp)
            
if n == 1 :
    print(top)
elif n == 2 : 
    print(max(tmpList1))
else :
    print(max(tmpList2))
    
        
        