# from queue import PriorityQueue 

# def solution(n, k, cmd):
#     l = []
#     for i in range(n):
#         l.append("X")
#     dq_1 = PriorityQueue()
#     dq_2 = PriorityQueue()
#     trash = []
#     for i in range(k):
#         dq_1.put(-i)
#     for i in range(k,n):
#         dq_2.put(i)
#     for i in cmd:
#         if len(i)>1:
#             splitted = i.split(" ")
#             command = splitted[0]
#             number = int(splitted[1])
#             if command == "U":
#                 for j in range(number):
#                     tmp = -dq_1.get()
#                     dq_2.put(tmp)
#             elif command == "D":
#                 for j in range(number):
#                     tmp = dq_2.get()
#                     dq_1.put(-tmp)
#         else:
#             command = i
#             if command == "C":
#                 trash.append(dq_2.get())
#                 if dq_2.empty():
#                     tmp = -dq_1.get()
#                     dq_2.put(tmp)
#             if command == "Z":
#                 num = trash.pop()
#                 tmp = dq_2.get()
#                 if num>=tmp:
#                     dq_2.put(tmp)
#                     dq_2.put(num)
#                 else:
#                     dq_2.put(tmp)
#                     dq_1.put(-num)
    
#     for i in range(dq_1.qsize()):
#         idx = -dq_1.get()
#         l[idx]="O"
#     for i in range(dq_2.qsize()):
#         idx = dq_2.get()
#         l[idx]="O"
#     answer = "".join(l)
#     return answer

# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])












from collections import deque

class Node:
    def __init__(self):
        self.prev = -1 # 이전 노드 인덱스
        self.next = -1 # 다음 노드 인덱스
        self.is_delete = False # 삭제 여부

def solution(n, k, cmd):
 
    # 1. 링크드리스트 초기화
    node_list = [Node() for _ in range(n)] # 노드 리스트 생성
    for i in range(n - 1):
        node_list[i].next = i + 1 # i 번째 노드의 next는 i+1
        node_list[i + 1].prev = i # i+1 번째 노드의 prev는 i
 
    # 2. 삭제된 노드를 저장할 스택
    del_stack = deque()
 
    # 3. 명령어 처리
    cur = k # 현재 가리키고 있는 노드의 인덱스
    for c in cmd:
 
        if len(c) > 1:
            c, move_size = c.split(' ')
            move_size = int(move_size)
 
        if c == "U":
            for i in range(move_size):
                cur = node_list[cur].prev # cur을 cur 노드의 prev로 교체
        elif c == "D":
            for i in range(move_size):
                cur = node_list[cur].next # cur을 cur 노드의 next로 교체
        elif c == "C":
            node_list[cur].is_delete = True # 현재 노드에 삭제 표시
            del_stack.append(cur) # 스택에 삭제된 노드 번호 추가
 
            prev_node = node_list[cur].prev # 이전 노드 번호
            next_node = node_list[cur].next # 다음 노드 번호
 
            if prev_node != -1: # 이전 노드가 있는 경우
                node_list[prev_node].next = next_node # 이전 노드의 next를 삭제된 노드가 가리키던 next로 교체
            if next_node != -1: # 다음 노드가 있는 경우
                node_list[next_node].prev = prev_node # 다음 노드의 prev를 삭제된 노드가 가리키던 prev로 교체
                cur = next_node # 가리키고 있는 노드를 next_node로 갱신
            else: # 만약 다음 노드가 없는 경우
                cur = prev_node # 가리키고 있는 노드를 prev_node로 갱신
 
        elif c == "Z":
            del_node = del_stack.pop() # stack의 가장 상위 요소를 가져옴
            node_list[del_node].is_delete = False # 해당 노드의 is_delete = False로 변경
 
            prev_node = node_list[del_node].prev # 삭제된 노드의 이전 노드
            next_node = node_list[del_node].next # 삭제된 노드의 다음 노드
 
            if prev_node != -1: # 이전 노드가 존재하는 경우
                node_list[prev_node].next = del_node # 이전 노드의 next를 현재 노드로 지정
            if next_node != -1:
                node_list[next_node].prev = del_node # 다음 노드의 prev를 현재 노드로 지정
 
    # 4. 삭제된 노드 판별
    answer = []
    for i in range(n):
        if node_list[i].is_delete: 
            answer.append("X")
        else: 
            answer.append("O")
    return "".join(answer)