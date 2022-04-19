N, M = map(int, input().split())
Board = []
count = []
for i in range(N):
    Board.append(input())
for a in range(N-7):
    for b in range(M-7):
        ErrorCount1 = 0
        ErrorCount2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if Board[i][j] != 'W':
                        ErrorCount1 += 1
                    if Board[i][j] != 'B':
                        ErrorCount2 += 1
                else:
                    if Board[i][j] != 'B':
                        ErrorCount1 += 1
                    if Board[i][j] != 'W':
                        ErrorCount2 += 1
        count.append(min(ErrorCount1, ErrorCount2))

result = min(count)
print(result)