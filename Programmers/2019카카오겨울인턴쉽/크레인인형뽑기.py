def solution(board, moves):
    stk = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                currentDoll = board[i][move-1]
                board[i][move-1] = 0
                if stk:
                    doll = stk.pop()
                    if doll==currentDoll :
                        answer += 2
                        break
                    else :
                        stk.append(doll)
                        stk.append(currentDoll)
                        break
                else :
                    stk.append(currentDoll)
                    break
    return answer