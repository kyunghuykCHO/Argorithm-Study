# def rotate90(twoDimensionList):
#     N = len(twoDimensionList)
#     rotatedList = [[0] * N for _ in range(N)]
#     for r in range(N):
#         for c in range(N):
#             rotatedList[c][N-1-r] = twoDimensionList[r][c]
#     return rotatedList

# def solution(key, lock):
#     answer = True
#     s = len(key)*2 + len(lock) - 2
#     m = [[2]*s for _ in range(s)]
#     for i in range(len(key)-1,s-2):
#         for j in range(len(key)-1,s-2):
#             if lock[i-2][j-2] == 0 :
#                 m[i][j] = 0
#             else :
#                 m[i][j] = 1

#     case1 = key
#     case2 = rotate90(key)
#     case3 = rotate90(rotate90(key))
#     case4 = rotate90(rotate90(rotate90(key)))
    
#     for i in range(len(key)+len(lock)-1):
#         for j in range(len(key)+len(lock)-1):
#             for k in range(i, i+len(key)): 
#                 for l in range(j, j+len(key)):
#                     if m[k][l] == case1[k-i][l-j] : answer = False
#                     # if m[k][l] == case2[k-i][l-j] : answer = False
#                     # if m[k][l] == case3[k-i][l-j] : answer = False
#                     # if m[k][l] == case4[k-i][l-j] : answer = False
#             if answer == True :
#                 return answer
#             answer = True
#             for k in range(i, i+len(key)): 
#                 for l in range(j, j+len(key)):
#                     # if m[k][l] == case1[k-i][l-j] : answer = False
#                     if m[k][l] == case2[k-i][l-j] : answer = False
#                     # if m[k][l] == case3[k-i][l-j] : answer = False
#                     # if m[k][l] == case4[k-i][l-j] : answer = False
#             if answer == True :
#                 return answer
#             answer = True
#             for k in range(i, i+len(key)): 
#                 for l in range(j, j+len(key)):
#                     # if m[k][l] == case1[k-i][l-j] : answer = False
#                     # if m[k][l] == case2[k-i][l-j] : answer = False
#                     if m[k][l] == case3[k-i][l-j] : answer = False
#                     # if m[k][l] == case4[k-i][l-j] : answer = False
#             if answer == True :
#                 return answer
#             answer = True
#             for k in range(i, i+len(key)): 
#                 for l in range(j, j+len(key)):
#                     # if m[k][l] == case1[k-i][l-j] : answer = False
#                     # if m[k][l] == case2[k-i][l-j] : answer = False
#                     # if m[k][l] == case3[k-i][l-j] : answer = False
#                     if m[k][l] == case4[k-i][l-j] : answer = False
#             if answer == True :
#                 return answer
    
#     return answer

# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))




# '''
# 2  2  2  2  2  2  2
# 2  2  2  2  2  2  2
# 2  2  1  1  1  2  2 
# 2  2  1  1  0  2  2
# 2  2  1  0  1  2  2 
# 2  2  2  2  2  2  2
# 2  2  2  2  2  2  2
# '''


























def rotate90(twoDimensionList):
    N = len(twoDimensionList)
    rotatedList = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotatedList[c][N-1-r] = twoDimensionList[r][c]
    return rotatedList

def solution(key, lock):
    answer = False
    s = len(key)*2 + len(lock) - 2
    m = [[2]*s for _ in range(s)]
    for i in range(len(key)-1,s-2):
        for j in range(len(key)-1,s-2):
            if lock[i-2][j-2] == 0 : m[i][j] = 0
            else : m[i][j] = 1

    case1 = key
    case2 = rotate90(key)
    case3 = rotate90(rotate90(key))
    case4 = rotate90(rotate90(rotate90(key)))
    
    for i in range(len(key)+len(lock)-1):
        for j in range(len(key)+len(lock)-1):
            
            cnt = 0
            for k in range(i, i+len(key)): 
                for l in range(j, j+len(key)):
                    if m[k][l] != 2 : cnt += 1
                    
            caseCnt1, caseCnt2, caseCnt3, caseCnt4 = 0, 0, 0, 0
            for k in range(i, i+len(key)): 
                for l in range(j, j+len(key)):
                    if m[k][l] != 2 :
                        if m[k][l] != case1[k-i][l-j] : caseCnt1+=1
                        if m[k][l] != case2[k-i][l-j] : caseCnt2+=1
                        if m[k][l] != case3[k-i][l-j] : caseCnt3+=1
                        if m[k][l] != case4[k-i][l-j] : caseCnt4+=1
            if caseCnt1 == cnt or caseCnt2 == cnt or caseCnt3 == cnt or caseCnt4 == cnt :
                answer = True
                return True
            
                    
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))




'''
2  2  2  2  2  2  2
2  2  2  2  2  2  2
2  2  1  1  1  2  2 
2  2  1  1  0  2  2
2  2  1  0  1  2  2 
2  2  2  2  2  2  2
2  2  2  2  2  2  2
'''