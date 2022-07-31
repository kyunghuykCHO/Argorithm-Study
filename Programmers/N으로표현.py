def solution(N, number):
    answer = [set([int(str(N)*i)]) for i in range(1, 9)]   # N을 각 인덱스별로 인덱스+1번 반복
    
    if N == number :
        return 1

    for i in range(1, 8) :      # 1에서 7까지
        for j in range(i) :
            for y in answer[j]:
                for x in answer[i-j-1] :    
                        answer[i].add(y+x)
                        answer[i].add(y*x)
                        answer[i].add(y-x)
                        if y > 0 :		# 0으로 수를 나누지 못하게
                            answer[i].add(x//y)
                if number in answer[i] :	# 찾으면
                    return i+1			# 인덱스가 0부터 시작이니까

    return -1			# 최솟값이 8보다 큼