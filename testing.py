# # # # [0,0,1,1,1,0,1,0,1,0,1,1]
# # # # [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

# # from collections import deque
# # def solution(infos, edges):
# #     global sheeps, wolfs
# #     answer = 0
    
# #     nodeMap = [[] for i in range(len(edges)+1)]
# #     for edge in edges:
# #         nodeMap[edge[0]].append(edge[1])
    
# #     visited = [False]*len(infos)
    
# #     sheep, wolf, currentNode = 1,0,0
# #     currentStatement = (sheep,wolf,currentNode)
    
# #     dq = deque([])
# #     dq.append(currentStatement)
# #     visited[currentStatement[2]] = True
# #     while dq:
# #         sheeps,wolfs,currentNode = dq.popleft() 
# #         print("===")
# #         print(sheeps,wolfs,currentNode)
# #         if infos[currentNode] == 1 :
# #             wolfs += 1
# #         if infos[currentNode] == 0 :
# #             sheeps += 1
# #         answer = sheeps
# #         for connectedNode in nodeMap[currentNode]:
# #             if visited[connectedNode] == False :
# #                 # 연결 노드에 양이 있을 때 
# #                 if infos[connectedNode] == 0 :
# #                     # 양이 늑대보다 많다
# #                     if sheeps+1 > wolfs :
# #                         dq.append((sheeps,wolfs,connectedNode))
# #                         visited[connectedNode] = True
# #                     # 늑대가 양보다 많다
# #                     if sheeps+1 <= wolfs :
# #                         dq.append((sheeps,wolfs,currentNode))
# #                 # 연결 노드에 늑대가 있을 때
# #                 if infos[connectedNode] == 1 :
# #                     # 양이 늑대를 앞설 때
# #                     if sheeps > wolfs + 1 :
# #                         dq.append((sheeps,wolfs,connectedNode))
# #                         visited[connectedNode] = True
# #                     # 늑대가 양보다 많거나 같을 때 
# #                     if sheeps <= wolfs+1 :
# #                         dq.append((sheeps,wolfs,currentNode))
    
# #     return answer+1

# # print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# # print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))






# # def dfs(sheeps, wolfs, currentNode, visited, nodeMap, infoes, answer):
# #     if sheeps > wolfs: 
# #         answer.append(sheeps)
# #         print("양이 더 많습니다")
# #         print(currentNode)
# #     else: 
# #         print("늑대가 더 많습니다")
# #         print(currentNode)
# #         return
    
# #     for nextNode in nodeMap[currentNode]:
# #         if not visited[nextNode]:
# #             visited[nextNode] = True
# #             if infoes[nextNode] == 0:
# #                 dfs(sheeps+1, wolfs, nextNode, visited, nodeMap, infoes, answer)            
# #             else:
# #                 dfs(sheeps, wolfs+1, nextNode, visited, nodeMap, infoes, answer)
# #     visited[currentNode] = False
            
            
# # def solution(infoes, edges):
# #     answer = []
# #     visited = [False for _ in range(len(infoes))]
# #     nodeMap = [[] for i in range(len(edges)+1)]
# #     for edge in edges:
# #         nodeMap[edge[0]].append(edge[1])
# #     visited[0] = True
# #     dfs(1, 0, 0, visited, nodeMap, infoes, answer)
# #     return max(answer)

# # print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# # print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))




def dfs(currentNode, sheep, wolf, nextNodes, info):
    global answer, nodeMap
    if info[currentNode] == 0:
        sheep += 1
        answer.append(sheep)
    else:
        wolf += 1
        
    if wolf >= sheep:
        return 
    
    nextNodes.extend(nodeMap[currentNode])
    for nextNode in nextNodes:
        tmp = []
        for n in nextNodes:
            if n != nextNode :
                tmp.append(n)
        dfs(nextNode, sheep, wolf, tmp, info)

    
    
def solution(info, edges):
    global answer, nodeMap
    answer = []
    nodeMap = [[] for _ in range(len(info))]
    
    for edge in edges:
        nodeMap[edge[0]].append(edge[1])
    
    dfs(0, 0, 0, [], info)
    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
# print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
