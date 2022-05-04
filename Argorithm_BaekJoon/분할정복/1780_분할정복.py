# def squareSearch(field,n):
#     global result_one
#     global result_minusone
#     global result_zero
#     count_one = 0
#     count_zero = 0
#     count_minusone = 0
#     for i in range(0,len(field)-n,n):
#         for j in range(0,len(field)-n,n):
#             divided = [m[j:j+n] for m in field[i:i+n]]
#             for k in divided:
#                 for l in k:
#                     if l == -1 :
#                         count_minusone += 1
#                     elif l == 0 :
#                         count_zero += 1
#                     elif l == 1 :
#                         count_one += 1
#             if count_one == n*n :
#                 result_one += 1
#             elif count_minusone == n*n :
#                 result_minusone += 1
#             elif count_zero == n*n :
#                 result_zero += 1
#             else :
#                 if n//3 != 0 :
#                     squareSearch(divided, int(n/3))


# N = int(input())
# field = []
# result_one = 0
# result_minusone = 0
# result_zero = 0
# for _ in range(N):
#     field.append(list(map(int,input().split())))
# squareSearch(field,int(N/3))
# print(result_minusone)
# print(result_zero)
# print(result_one)

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

neg = 0
neut = 0
pos = 0

def clip_paper(x, y, n):
    global neg, neut, pos
    
    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if(paper[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n//3, y + l * n//3, n//3)
                return
            
    if(num_check == -1):
        neg += 1
    elif(num_check == 0):
        neut += 1
    else:
        pos += 1
        
clip_paper(0, 0, N)
print(f'{neg}\n{neut}\n{pos}')