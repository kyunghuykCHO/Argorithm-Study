# def solution1(sequence, k):
#     dp = [[0]*2 for _ in range(len(sequence))]
#     sum = sequence[0]
#     if sequence[0] == k :
#         return [0,0]
    
#     for i in range(1,len(sequence)):
#         endIndex = i
#         sum += sequence[i]
#         if sum >= k :
#             sum2 = 0
#             flag = False
#             for j in range(i,-1,-1):
#                 sum2 += sequence[j]
#                 if sum2 == k :
#                     startIndex = j
#                     flag = True
#             if flag == True and dp[i-1][1] != 0:
#                 tmp1 = dp[i-1][1] - dp[i-1][0]
#                 tmp2 = endIndex - startIndex
#                 if tmp1 <= tmp2 :
#                     dp[i] = dp[i-1]
#                 else :
#                     dp[i] = [startIndex,endIndex]
#             if flag == True and dp[i-1][1] == 0:
#                 dp[i] = [startIndex,endIndex]
#             if flag == False:
#                 dp[i] = dp[i-1]
#     print(dp)
#     return dp[-1]

'''
1 1 3 3 5 
k = 5 
'''



# def solution2(sequence, k):
#     answers = []
#     sum = 0
#     l = 0
#     r = -1
    
#     while True:
#         if sum < k:
#             r += 1
#             if r >= len(sequence):
#                 break
#             sum += sequence[r]
#         else:
#             sum -= sequence[l]
#             if l >= len(sequence):
#                 break
#             l += 1
#         if sum == k:
#             answers.append([l, r])
    
#     answers.sort(key=lambda x: (x[1]-x[0], x[0]))
#     return answers[0]


def solution(sequence, k):
    answer = []    
    sum = sequence[0]
    startingPoint = 0
    endPoint = 0
    
    if k == sum :
        return [0,0]
    
    while True:
        if sum > k :
            sum -= sequence[startingPoint]
            startingPoint += 1
            if startingPoint == len(sequence): break
        elif sum <= k :
            endPoint += 1 
            if endPoint == len(sequence): break
            sum += sequence[endPoint]
        if sum == k :
            answer.append([startingPoint,endPoint])
            
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]


print(solution([1,2,3,4,5],7))
print(solution([2, 2, 2, 2, 2],6))