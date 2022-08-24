# [알고력, 코딩력, 증가알고력, 증가코딩력, 시간]

from collections import deque 

def solution(alp, cop, problems):
    
    # 한 문제만 주어진 경우 
    if len(problems)==1:
        if alp>=problems[0] and cop>=problems[1]:
            return 0
        elif alp<problems[0] and cop>=problems[1]:
            return problems[0]-alp
        
        elif alp>=problems[0] and cop<problems[1]:
            return problems[1]-cop
        else:
            return (problems[0]-alp) + (problems[1]-cop)
    
    # 문제가 두 문제 이상인 경우
    problems.sort(key=lambda x: (x[0], x[1]))
    dq = deque()
    for problem in problems:
        dq.append(problem)
    
    max_alp = 0
    max_cop = 0
    for problem in problems:
        if max_alp < problem[0] :
            max_alp = problem[0]
        if max_cop < problem[1] :
            max_cop = problem[1]
            
    dp = [[0]*(max_alp+30) for _ in range(max_cop+30)]
    for i in range(cop,len(dp)):
        for j in range(alp,len(dp[0])):
            dp[i][j] = i-cop+j-alp
    while dq:
        problem = dq.popleft()
        for i in range(problem[1],len(dp)):
            for j in range(problem[0],len(dp[0])):
                row = i+problem[3] 
                col = j+problem[2]
                if row >= max_cop and col >= max_alp:
                    dp[max_cop][max_alp] = min(dp[max_cop][max_alp],dp[i][j]+problem[4])
                elif 0<=row<len(dp) and 0<=col<len(dp[0]):
                    dp[row][col] = min(dp[row][col], dp[i][j] + problem[4])
                # elif row >= max_cop and 0<=col<max_alp:
                #     dp[max_cop][col] = min(dp[max_cop][col],dp[i][j]+problem[4])
                # elif 0<= row < max_cop and col >= max_alp:
                #     dp[row][max_alp] = min(dp[row][max_alp],dp[i][j]+problem[4])
    return dp[max_cop][max_alp]
    
solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])
solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])












# def solution(alp,cop,problems) :
#     INF = 1e9
#     dp = [[INF]*162 for _ in range(162)]
#     alpMax = 0
#     copMax = 0
#     for problem in problems:
#         alpMax = max(problem[0], alpMax)
#         copMax = max(problem[1], copMax)
    
    
#     if alp>=alpMax and cop>=copMax:
#         return 0
#     if alp>=alpMax:
#         alp = alpMax
#     if cop>=copMax:
#         cop = copMax
    
#     dp[alp][cop] = 0
        
#     for i in range(alp,160):
#         for j in range(cop,160):
#             dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
#             dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
#             for k in range(len(problems)):
#                 if i+problems[k][2] > alpMax :
#                     alq_rwd = alpMax
#                 else:
#                     alq_rwd = i+problems[k][2]
#                 if j+problems[k][3] > copMax :
#                     cop_rwd = copMax
#                 else:
#                     cop_rwd = j+problems[k][3]
#                 cost = problems[k][4]
                
#                 if(i >= problems[k][0] and j >= problems[k][1] ):
#                     dp[alq_rwd][cop_rwd] = min(dp[alq_rwd][cop_rwd], dp[i][j] + cost)
#     return dp[alpMax][copMax]