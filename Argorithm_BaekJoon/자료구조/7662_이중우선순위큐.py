import heapq  
T = int(input())
for _ in range(T):
    N = int(input())
    answer = []
    max_list = []
    for i in range(N):
        a,b = map(str,input().split())
        if a == "I":
            heapq.heappush(answer, int(b))
        elif a == "D":
            if b == "1":
                if len(answer) == 0:
                    continue
                for j in range(len(answer)):
                    tmp = heapq.heappop(answer)
                    heapq.heappush(max_list, (-tmp,tmp))
                heapq.heappop(max_list)[1]
                for j in range(len(max_list)):
                    tmp = heapq.heappop(max_list)[1]
                    heapq.heappush(answer,tmp)
            else:
                if len(answer) == 0:
                    continue
                heapq.heappop(answer)
    if len(answer)==0:
        print("EMPTY")
        
    elif len(answer) == 1:
        print(answer[0])
    
    else:
        answer.sort(reverse=True)
        print(answer[0], answer[-1])