import sys
sys.setrecursionlimit(10**8)
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
move = ['d', 'l', 'r', 'u'] 
answer = 'z'
def dfs(n, m, x, y, r, c, path, distance, k):
    global answer
    if k < distance + abs(x - r) + abs(y - c):
        return
    if x == r and y == c and distance == k:
        answer = path
        return 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m and path < answer:
            dfs(n, m, nx, ny, r, c, path+move[i], distance + 1, k)

def solution(n, m, x, y, r, c, k):
    if k < abs(x - r) + abs(y - c) :
        return "impossible"
    if (k - (abs(x - r) + abs(y - c))) % 2 != 0 :
        return "impossible"
    dfs(n, m, x, y, r, c, "", 0, k)
    return answer