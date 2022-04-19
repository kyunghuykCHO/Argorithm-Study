# 동전의 종류는 N 종류, 동전의 개수는 多
# 각 동전을 이용해서 가치의 합을 K 로 만들고자 함 
# 이때 필요한 동전의 개수의 최소값 구하기 ! 

N,K = map(int, input().split())
Nlist = []
for i in range(N):
    Nlist.append(int(input()))
Nlist.sort()
Nlist.reverse()

result = 0

for j in Nlist:
    if K//j > 0:
        result+=K//j
        K = K%j

print(result)