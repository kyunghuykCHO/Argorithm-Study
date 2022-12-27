from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse = True) # 내림차순 정렬
    dq = deque(people) # deque 에 삽입
    while dq:
        if len(dq)>=2: # 남은 인원이 2명 이상이라면 
            mostHeavyPerson = dq.popleft() # 제일 무거운 사람 뽑고
            mostLightPerson = dq.pop() # 제일 가벼운 사람 뽑고 
            if (limit - mostHeavyPerson)>= mostLightPerson: # 두명 다 탈 수 있다면 
                answer+=1 # 태운다 answer +=1 
            else:
                dq.append(mostLightPerson) # 다 못태운다면 가벼운사람은 다시 deque에 넣어주고
                answer+=1 # 무거운 사람만 뽑힌채로 answer += 1
        else: # 남은 인원이 한명이라면 
            dq.pop() # 그냥 보트에 태우고
            answer+=1 # answer += 1
    
    return answer

print(solution([70, 80, 50], 100))
