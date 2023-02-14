import heapq

def solution(n, k, enemy):
    answer = 0
    deathToll = 0
    hp = []
    
    for e in enemy:
        heapq.heappush(hp, -e)
        deathToll += e
        answer += 1
        if deathToll > n :
            if k == 0 :
                answer -= 1
                break
            else :
                deathToll += heapq.heappop(hp) # 제일 큰수 뺀다??
                k -= 1
    return answer

print(solution(7,3,[4, 2, 4, 5, 3, 3, 1]))
print(solution(2,4,[3,3,3,3]))