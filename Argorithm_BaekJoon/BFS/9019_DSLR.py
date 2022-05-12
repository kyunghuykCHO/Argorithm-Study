#  이문제는 dfs문제인거 같다.
import sys
input = sys.stdin.readline
from collections import deque


t = int(input())

def order(num, case):
    if case == 'D':
        # n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 
        # 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
        return (int(num) * 2) % 10000
    elif case =='S':
        # n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
        return (int(num)-1) % 10000
    elif case == 'L':
        # n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 
        # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
        tmp = num // 1000
        return num % 1000 * 10 + tmp
    elif case == 'R':
        # n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 
        # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
        tmp = num % 10
        return num // 10 + 1000 * tmp

# for문을 돌아서 다음 경우를 확인 해줄 리스트 
# 일반 BFS 문제에서 dx,dy 역할
d = ['D','S','L','R']

def bfs(a,b,visited):
    # a와 빈 문자열을 q에 넣어주고 시작.
    q = deque([[a,""]])
    # a 는 방문처리
    visited[a] = 1
    # BFS 시작
    while q:
        num, case = q.popleft()
        if num == b:
            print(case)
            break
        # 현재숫자에서  D,S,L,R 을 적용해보고 가능한 숫자를 구해준다.
        for i in range(4):
            n_case = order(num,d[i])
            if visited[n_case] == 0:
                # 가능한 숫자가 있다면, 가능한 숫자와 가능하게 한 문자를 처음 "" 로 시작한 문자열 뒤에 붙여준다.
                q.append((n_case,case+d[i]))
                visited[n_case] = 1

for _ in range(t):
    # 조건에서  10000 미만이라고 했으니, 10000으로 초기화 해준다.
    visited=[0 for _ in range(10000)]
    a,b = map(int,input().split())
    bfs(a,b,visited)