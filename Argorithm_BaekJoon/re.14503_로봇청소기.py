N,M = map(int,input().split())
r,c,d = map(int,input().split())
field = []
for i in range(N):
    field.append(list(map(int,input().split())))
field[r][c] = 2

def change(d):
    if d==0 :
        d = 3 
    if d==1 :
        d = 0
    if d==2 :
        d = 1
    if d==3 :
        d = 2
    return d 

