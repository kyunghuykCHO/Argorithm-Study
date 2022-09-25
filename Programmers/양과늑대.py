from collections import deque

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    answer = 0
    for edge in edges:
        graph[edge[0]].append(edge[1])
    dq = deque([])
    dq.append((0,1,0,set()))
    while dq:
        node, sheep, wolf, nextNode = dq.popleft()
        answer = max(answer,sheep)
        nextNode.update(graph[node]) 
        for next in nextNode:
            if info[next] == 1:
                if sheep != wolf + 1:
                    dq.append((next,sheep,wolf+1, nextNode - {next}))
            else:
                dq.append((next,sheep+1,wolf, nextNode - {next}))
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))