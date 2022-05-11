import heapq

def solution(operations):
    answer = []
    max_list = []
    for i in operations:
        a = i.split()
        if a[0] == "I":
            heapq.heappush(answer, int(a[1]))
        elif a[0] == "D":
            if a[1] == "1":
                if len(answer) == 0:
                    continue
                for i in range(len(answer)):
                    tmp = heapq.heappop(answer)
                    heapq.heappush(max_list, (-tmp,tmp))
                heapq.heappop(max_list)[1]
                for i in range(len(max_list)):
                    tmp = heapq.heappop(max_list)[1]
                    heapq.heappush(answer,tmp)
            else:
                if len(answer) == 0:
                    continue
                heapq.heappop(answer)
    if len(answer)==0:
        answer.append(0)
        answer.append(0)
    answer.sort(reverse=True)
    result = []
    result.append(answer[0])
    result.append(answer[-1])
    return result

operations = ["I 4", "I -1", "I 6", "I 3"]
solution(operations)

    
    