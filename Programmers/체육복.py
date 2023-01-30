def solution(n, lost, reserve):
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)
    answer = n - len(lostSet)

    for reserve in reserveSet:
        if reserve-1 in lostSet: 
            lostSet.remove(reserve-1)
            answer += 1
        elif reserve+1 in lostSet:
            lostSet.remove(reserve+1)
            answer += 1
    return answer