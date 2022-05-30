def solution(players, starting, power):
    if starting+2 < len(players):
        # print("첫 if문 입장")
        if players[starting]<=power and players[starting+1]<=power+1 and players[starting+2]<=power+3:
            # print("3승 발견")
            power += 6
            upgrade = 3
            i = starting+3
            while i< len(players) and players[i] <= power:
                # print("3승 후 --> 1승 추가")
                upgrade +=1
                power += upgrade
                i+=1
            if i<len(players):
                # print("공간 남았음")
                starting = i
                solution(players, starting, power)
            else:
                # print("남은 경기 전승 후 power return")
                # print("결과")
                # print(power)
                return power
        else:
            # print("3승을 할 수 없으므로 패합니다.")
            power+=k
            starting+=1
            solution(players,starting,power)
        
    else:
        for i in range(len(players)-starting):
            power += k
        return power

players = [1,2,4,7]
power = 1
k = 2
starting = 0

print(solution(players,starting,power))