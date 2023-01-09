N = int(input())
answer = [["*" for j in range(N)] for i in range(N)]

def solution(startRow, startCol, N):
    if N>=9 :
        N = N//3
        
        for i in range(startRow+N, startRow+N*2):
            for j in range(startCol+N, startCol+N*2):
                answer[i][j] = " "
                
        solution(startRow, startCol, N)
        solution(startRow, startCol+N, N)
        solution(startRow, startCol+2*N, N)
        solution(startRow+N, startCol, N)
        solution(startRow+N, startCol+2*N, N)
        solution(startRow+2*N, startCol, N)
        solution(startRow+2*N, startCol+N, N)
        solution(startRow+2*N, startCol+2*N, N)
        
    elif N == 3 :
        answer[startRow+1][startCol+1] = " "

    return answer

solution(0,0,N)


# 출력 
for line in answer:
    print(''.join(line))



'''
3
***
* * 2
***

9
*********
* ** ** *
*********
***   *** 4
* *   * *
***   *** 6
*********
* ** ** *
*********

27
*************************** 0    *** 을 9번
* ** ** ** ** ** ** ** ** * 1    * * 을 9번
*************************** 2    *** 을 9번
***   ******   ******   *** 3
* *   * ** *   * ** *   * * 4
***   ******   ******   *** 5
*************************** 6
* ** ** ** ** ** ** ** ** * 7
*************************** 8
*********         ********* 9
* ** ** *         * ** ** * 10
*********         ********* 11
***   ***         ***   *** 12
* *   * *         * *   * * 13
***   ***         ***   *** 14
*********         ********* 15 
* ** ** *         * ** ** * 16
*********         ********* 17
*************************** 18
* ** ** ** ** ** ** ** ** *
*************************** 21
***   ******   ******   *** 
* *   * ** *   * ** *   * *
***   ******   ******   *** 
*************************** 25
* ** ** ** ** ** ** ** ** *
*************************** 26

'''