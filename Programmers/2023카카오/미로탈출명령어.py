# def solution(n, m, x, y, r, c, k):
#     stk = []
#     stk.append((x,y,0,''))
#     while stk:
#         row,col,distance,path = stk.pop()
#         remain = k-distance
#         if row == r and col == c and remain == 0 :
#             return path
#         if row == r and col == c and remain%2 != 0 :
#             return 'impossible'
#         if row == r and col == c and remain > 0 :
#             if r < n :
#                 if n - r >= (remain//2) :
#                     path += "d"*(remain//2)
#                     path += "u"*(remain//2)
#                     return path
#                 else : 
#                     stk.append((row+(n-r),col,distance+(n-r),path+'d'*(n-r)))
                
#             elif 1 < c :
#                 if c - 1 >= (remain//2) :
#                     path += "l"*(remain//2)
#                     path += "r"*(remain//2)
#                     return path
#                 else : 
#                     stk.append((row,col-(c-1),distance+(c-1)),path+'l'*(c-1))
                
#             elif c < m :
#                 if m - c >= (remain//2) :
#                     path += "r"*(remain//2)
#                     path += "l"*(remain//2)
#                     return path
#                 else : 
#                     stk.append((row,col+(m-c),distance+(m-c),path+'r'*(m-c)))
#             elif 1 < r : 
#                 if r - 1 >= (remain//2) :
#                     path += "u"*(remain//2)
#                     path += "d"*(remain//2)
#                     return path
#                 else : 
#                     stk.append((row-(r-1),col,distance+(r-1),path+'u'*(r-1)))
        
#         if r > row : 
#             stk.append((row+1,col,distance+1,path+'d'))
#         elif c < col :
#             stk.append((row,col-1,distance+1,path+'l'))
#         elif c > col : 
#             stk.append((row,col+1,distance+1,path+'r'))
#         elif r < row : 
#             stk.append((row-1,col,distance+1,path+'u'))









# import sys
# sys.setrecursionlimit(10**8)
# dx = [1, 0, 0, -1]
# dy = [0, -1, 1, 0]
# move = ['d', 'l', 'r', 'u'] 
# answer = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
# def dfs(n, m, x, y, r, c, path, distance, k):
#     print(path)
#     global answer
#     if k < distance + abs(x - r) + abs(y - c):
#         return
#     if x == r and y == c and distance == k:
#         answer = path
#         return 
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 1 <= nx <= n and 1 <= ny <= m and path < answer:
#             dfs(n, m, nx, ny, r, c, path+move[i], distance + 1, k)

# def solution(n, m, x, y, r, c, k):
#     if k < abs(x - r) + abs(y - c) :
#         return "impossible"
#     if (k - (abs(x - r) + abs(y - c))) % 2 != 0 :
#         return "impossible"
#     dfs(n, m, x, y, r, c, "", 0, k)
#     return answer



import sys
sys.setrecursionlimit(10**8)
move = {"d":[1,0], "l":[0,-1], "r":[0,1], "u":[-1,0]}
answer = 'z'
def dfs(n, m, cur, target, depth):
    global answer
    y, x, path, grid_depth = cur
    if depth < grid_depth + abs(x - target[1]) + abs(y - target[0]):
        return
    if (y,x)==target and grid_depth==depth:
        answer = path
        return 
    
    for direction in move:
        dy, dx = move[direction]
        ny = dy + y
        nx = dx + x

        if 0<=ny<=n and 0<=nx<=m and grid_depth<depth and path < answer:
            dfs(n, m, (ny, nx, path+direction, grid_depth+1), target, depth)
        
def solution(n, m, x, y, r, c, k):
    if k < abs(x - r) + abs(y - c) :
        return "impossible"
    if (k - (abs(x - r) + abs(y - c))) % 2 != 0 :
        return "impossible"
    dfs(n-1, m-1, (x-1, y-1, '', 0), (r-1, c-1), k)
    
    return answer

print(solution(6, 6, 2,	6, 6, 5, 11))

# print(solution(3,4,2,3,3,1,1))
# print(solution(2,2,1,1,2,2,2))
# print(solution(3,3,1,2,3,3,4))
# print(solution(6,6,2,6,6,5,11))


