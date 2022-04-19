# def cut_paper(arr, result):
#     n = len(arr)//2
#     for i in range(len(arr)-n):
#         for j in range(len(arr)-n):
#             tmp = [row[j:j+n] for row in arr[i:i+n]]
#             l = len(tmp)
#             blue = 0
#             white = 0
#             for k in tmp:
#                 for m in k:
#                     if m == 1:
#                         blue+=1
#                     else:
#                         white+=1
#             if blue == l*l:
#                 result.append(1)
#             elif white == l*l:
#                 result.append(0)
#             else:
#                 cut_paper(tmp,result)
# N = int(input())
# paper = []
# result = []
# for i in range(N):
#     paper.append(list(map(int,input().split())))
# cut_paper(paper, result)
# print(result.count(0))
# print(result.count(1))

import sys
N=int(sys.stdin.readline())
paper = []
result = []
for i in range(N):
    paper.append(list(map(int,input().split()))) 
 
def cut(x,y,n, result):
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                cut(x,y,n//2,result)
                cut(x,y+n//2,n//2,result)
                cut(x+n//2,y,n//2,result)
                cut(x+n//2,y+n//2,n//2,result)
                return

    if check==0:
        result.append(0)
        return
    else:  
        result.append(1)
        return

 
 
cut(0,0,N, result)
print(result.count(0))
print(result.count(1))