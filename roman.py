rom1 = {"I":1, "V":5, "X":10, "L":50, "C":100}
rom2 = {"IV":4, "IX":9, "XL":40, "XC":90}

strList = list(input())
result = 0

cnt = 0
while(cnt<len(strList)) :
    if(cnt+1<len(strList) and (strList[cnt]+strList[cnt+1]) in rom2) :
        result += rom2.get(strList[cnt]+strList[cnt+1])
        cnt+=2
    
    else : 
        result += rom1.get(strList[cnt])
        cnt+=1
        
print(result)
    