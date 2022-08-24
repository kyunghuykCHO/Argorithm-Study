def solution(n, info):
    answer = [0 for _ in range(len(info))]
    score = 0
    for i in range(len(info)):
        if info[i] >=1:
            score += (10-i)
    
    for i in range(len(info)):
        if n >=1:
            answer[i] = info[i]+1
            n-=answer[i]
    
    

    
    
    return answer

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
