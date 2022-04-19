# import numpy as np
# from itertools import combinations

# def solution(relation):
#     answer = 0
#     relation = np.array(relation).T 
#     candidates = []

#     for grouping_num in range(1, len(relation)+1):
#         comb = list(combinations([relation[i] for i in range(len(relation))], grouping_num))  
#         index_comb = list(combinations([i for i in range(len(relation))], grouping_num)) 
#         for c in range(len(comb)): 
#             group = []
#             for i in range(len(comb[c][0])): 
#                 group.append(tuple(comb[c][j][i] for j in range(len(comb[c]))))
#             if len(group) == len(set(group)):
#                 candidates.append(set(index_comb[c]))

#     for c in range(len(candidates[::-1])): 
#         check = True
#         for i in range(c): 
#             if candidates[i].issubset(candidates[c]):
#                 check = False
#                 break
#         if check:
#             answer += 1

#     return answer

from itertools import combinations

def solution(relation):
    row,col = len(relation),len(relation[0])  
    
    candidates = []
    for i in range(1, col+1): 
        candidates.extend(combinations(range(col), i))
    
    unique = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp))==row: 
            unique.append(keys)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i])==len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])            
    return len(answer)