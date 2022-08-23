# 길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다. 
# 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 
# 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.

# from collections import deque

# def DFS(visit,queue1,queue2,length):
#     goal = (sum(queue1)+sum(queue2))//2
#     dx = [1,0]
#     dy = [0,1]
#     move = int(1e9)
#     dq = deque()
#     row = 0
#     col = 0
#     dq.append((row,col,sum(queue1[row:])+sum(queue2[:col])))
#     while dq:
#         r,c,summary = dq.popleft()
#         visit[r][c] = True
#         if summary == goal and r+c < move:
#             move = r+c
#         for i in range(2):
#             nr = r + dx[i]
#             nc = c + dy[i]
#             if 0<=nr<length and 0<=nc<length and visit[nr][nc]==False:
#                 visit[nr][nc] = True
#                 dq.append((nr,nc,sum(queue1[nr:])+sum(queue2[:nc])))
#     if move == int(1e9):
#         return -1
#     else:
#         return move
    
    
# def solution(queue1, queue2):
#     length = len(queue1)+1
#     visit = [[False]*(length) for _ in range(length)]
#     answer = DFS(visit,queue1,queue2,length)
#     return answer

# print(solution([3, 2, 7, 2],[4, 6, 5, 1]))





# from collections import deque

# def DFS(visit,dq1,dq2,length):
#     goal = (sum(dq1)+sum(dq2))//2
#     dx = [1,0]
#     dy = [0,1]
#     move = int(1e9)
#     dq = deque()
#     dq.append((0,0,dq1,dq2))
#     while dq:
#         r,c,dq1,dq2 = dq.popleft()
#         visit[r][c] = True
#         for i in range(r):
#             if dq1:
#                 tmp = dq1.popleft()
#                 dq2.append(tmp)
#         for i in range(c):
#             if dq2:
#                 tmp = dq2.popleft()
#                 dq1.append(tmp)
                
#         print("r = {} and dq1 = {}".format(r,dq1))
#         print("c = {} and dq2 = {}".format(c,dq2))

#         if sum(dq1) == goal and r+c < move:
#             move = r+c
#         for i in range(2):
#             nr = r + dx[i]
#             nc = c + dy[i]
#             if 0<=nr<length and 0<=nc<length and visit[nr][nc]==False:
#                 visit[nr][nc] = True
#                 dq.append((nr,nc,dq1,dq2))
#     if move == int(1e9):
#         return -1
#     else:
#         return move
    
    
# def solution(queue1, queue2):
#     dq1 = deque(queue1)
#     dq2 = deque(queue2)
#     length = len(queue1)*2+1
#     visit = [[False]*(length) for _ in range(length)]
#     answer = DFS(visit,dq1,dq2,length)
#     return answer


from collections import deque

def solution(queue1, queue2):
    qu_1 = deque(queue1)
    qu_2 = deque(queue2)
    sum_1 = sum(qu_1)
    sum_2 = sum(qu_2)

    for i in range(len(queue1) * 3):
        if sum_1 == sum_2:
            return i
        if sum_1 > sum_2:
            num = qu_1.popleft()
            qu_2.append(num)
            sum_1 -= num
            sum_2 += num
        else:
            num = qu_2.popleft()
            qu_1.append(num)
            sum_2 -= num
            sum_1 += num
    return -1

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))