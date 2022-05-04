# # 첫번째 COIN 문제
# from collections import deque
# m = 2
# v = [1,2,3,1]
# dq = deque([])
# for i in range(len(v)):
#     dq.append(v[i])
# result = [0]*m  
# while dq:
#     coin = dq.popleft()
#     if len(set(result)) == 1:
#         result[0] += coin
#     else:
#         idx = result.index(min(result))
#         result[idx] += coin
# print(min(result))

# # 우선순위 Q 를 이용한 방법
# import heapq
# def solution(m,v):
#     answer = 0
#     L = list()
#     tmp = 100000000
#     for i in range(len(v)):
#         if len(L)>=m:
#             tmp = i
#             break
#         heapq.heappush(L,v[i])
#     for i in range(tmp,len(v)):
#         tmpnum = heapq.heappop(L)
#         tmpnum += v[i]
#         heapq.heappush(L,tmpnum)
#     answer = min(L)
#     return answer

# ==================================================

students = ["AAALLLAPAA", "AAAAAAAPPP", "ALAAAAPAAA"]
res = []
for i in range(len(students)):
    res.append([10,i+1])
for i in range(len(students)):
    Acount = 0
    Lcount = 0
    Pcount = 0
    for j in students[i]:
        if j=='A':
            Acount += 1
        elif j=='L':
            Lcount += 1
        else :
            Pcount += 1
    p = Lcount//2
    Pcount+=p
    if Pcount>=3:
        res[i][0] = 0
        continue
    else :
        res[i][0] += Acount
        res[i][0] -= Pcount

res.sort(key = lambda x: (x[0],x[1]))
print(res)