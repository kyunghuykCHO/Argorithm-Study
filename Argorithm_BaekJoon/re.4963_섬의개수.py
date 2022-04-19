from collections import deque

M,N,K = map(int,input().split())
field = [[1]*N for _ in range(M)]
results = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            field[j][k] = 0

for i in range(M):
    for j in range(N):
        count = 0
        if field[i][j] == 1:
            field[i][j]=0
            queue = deque([])
            queue.append([i, j])
            count+=1

            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    Y = y + dy[k]
                    X = x + dx[k]

                    if 0 <= X < N and 0 <= Y < M and field[Y][X] == 1:
                        field[Y][X] = 0
                        queue.append([Y, X])
                        count += 1

            results.append(count)

results.sort()
print(len(results))
for result in results:
    print(result,end=' ')