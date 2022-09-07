def dfs(col,row,map,dp,m,n,dx,dy) :
    if col == m-1 and row == n-1:
        return 1
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    count = 0
    for i in range(2):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1:
            count += dfs(ny, nx,map,dp,m,n,dx,dy)
    dp[row][col] = count
    return dp[row][col]
    

def solution(m, n, puddles):
    map = [[0]*m for _ in range(n)]
    for puddle in puddles:
        map[puddle[1]-1][puddle[0]-1] = 1
    dp = [[-1] * m for _ in range(n)]
    dx, dy = [1,0], [0,1]
    answer = dfs(0,0,map,dp,m,n,dx,dy)
    return answer%1000000007



print(solution(4,3,[[2, 2]]))