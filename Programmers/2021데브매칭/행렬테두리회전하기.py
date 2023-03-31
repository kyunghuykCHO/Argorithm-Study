def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns)] for j in range(rows)]
    cnt = 1
    for row in range(rows):
        for column in range(columns):
            matrix[row][column] = cnt
            cnt += 1
            
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        
        tmp1 = matrix[x1][y1]
        minimum = tmp1
        
        for i in range(x1,x2):
            tmp2 = matrix[i+1][y1]
            matrix[i][y1] = tmp2
            minimum = min(minimum, tmp2)

        for i in range(y1,y2):
            tmp2 = matrix[x2][i+1]
            matrix[x2][i] = tmp2
            minimum = min(minimum, tmp2)

        for i in range(x2,x1,-1):
            tmp2 = matrix[i-1][y2]
            matrix[i][y2] = tmp2
            minimum = min(minimum, tmp2)

        for i in range(y2,y1,-1):
            tmp2 = matrix[x1][i-1]
            matrix[x1][i] = tmp2
            minimum = min(minimum, tmp2)

        matrix[x1][y1+1] = tmp1
        answer.append(minimum)

            
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))