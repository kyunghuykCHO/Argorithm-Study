def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        sett = set()
        sett.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for operation1 in dp[j]:
                for operation2 in dp[-j-1]:
                    sett.add(operation1 + operation2)
                    sett.add(operation1 - operation2)
                    sett.add(operation1 * operation2)
                    
                    if operation2 != 0:
                        sett.add(operation1 // operation2)

        if number in sett:
            answer = i
            break
        
        dp.append(sett)

    return answer


print(solution(3,32))