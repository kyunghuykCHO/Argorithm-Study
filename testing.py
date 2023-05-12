from collections import deque, defaultdict

def bfs(computer, visited, network):
    if visited[computer]:
        return 0
    
    deq = deque([computer])
    
    while deq:
        node = deq.popleft()
        
        if visited[node]:
            continue
        
        visited[node] = True
        
        for next_node in network[node]:
            deq.append(next_node)
    
    return 1
        
        
def solution(n, computers):
    answer = 0
    visited = [False]*n
    network = defaultdict(list)
    
    # 초기화 코드 
    for i in range(len(computers)):
        network[i] = []
        for j in range(len(computers[0])):
            if computers[i][j]==1 and i!=j:
                network[i].append(j)

    # 노드 돌면서 연결 배열 뽑아서 BFS 
    for computer in network:
        answer += bfs(computer, visited, network)
        
    return answer