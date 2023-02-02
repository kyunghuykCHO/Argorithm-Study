# def solution(scores):
#     tmpScore = copy.deepcopy(scores)
#     tmpScore[0].append(-1)
#     tmpScore.sort(key=lambda x: (x[0]))
#     for i in range(len(tmpScore)):
#         if len(tmpScore[i]) == 3:
#             atScore = tmpScore[i][0]
#             evScore = tmpScore[i][1]
#             for j in range(i+1,len(tmpScore)):
#                 if tmpScore[j][0] > atScore and tmpScore[j][1] > evScore :
#                     return -1
                
#     for score in scores:
#         score.append(score[0]+score[1])
#     scores[0].append(-1)
#     scores.sort(reverse = True, key=lambda x: (x[2]))
    
#     maxScore = scores[0][2]
#     grade = 1
#     equal = 1
#     for i in range(1, len(scores)):
#         if len(scores[i])==3 and scores[i][2] < maxScore :
#             maxScore = scores[i][2]
#             grade += equal
#             equal = 1
#         if len(scores[i])==3 and scores[i][2] == maxScore : 
#             equal += 1
#         if len(scores[i])==4 and scores[i][2] == maxScore :
#             return grade
#         if len(scores[i])==4 and scores[i][2] < maxScore :
#             return grade + equal
        
#     return answer






def solution(scores):
    answer = 1
    myEtScore = scores[0][0]
    myEvScore = scores[0][1]
    scores.sort(key = lambda x : (-x[0], x[1]))
    print(scores)
    prevEvScore = 0
    for score in scores:
        etScore = score[0]
        evScore = score[1]
        if etScore > myEtScore and evScore > myEvScore:
            return -1
        
        if prevEvScore <= evScore :
            if evScore+etScore > myEtScore + myEvScore :
                answer+=1
            prevEvScore = evScore
            
    return answer

print(solution([[3,3],[2,5],[6,3],[6,3],[5,2],[1,4]]))

# 5 2    4 3    2 3    
