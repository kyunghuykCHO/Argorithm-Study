N = int(input())
F = []
for i in range(N):
    F.append(list(input()))    
result = []

def cutting(x, y, n):
    num_check = F[x][y]
    cnt = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if(F[i][j] != num_check):
                cnt+=1
                result.append("(")
                cutting(x,y,n//2)
                cutting(x,y+n//2,n//2)
                cutting(x+n//2,y,n//2)
                cutting(x+n//2,y+n//2,n//2)
                result.append(")")
                return
    if cnt==0 and num_check == "1":
        result.append("1")
    if cnt==0 and num_check == "0":
        result.append("0")

cutting(0,0,N)
result = "".join(result)
print(result)