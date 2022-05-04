from collections import deque

def test1(p):
    dq = deque([])
    leftCnt = 0
    rightCnt = 0
    stack = []

    for i in p:
        dq.append(i)
    while True:
        n = dq.popleft()
        if n == "(" :
            stack.append(n)
            leftCnt += 1
        else :
            stack.append(n)
            rightCnt += 1
        if leftCnt == rightCnt :
            u = ''.join(stack)
            v = ''.join(dq)
            break
    return u, v

def test2(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return 1
            stack.pop()

    return 0

def solution(p):
    if p=="":
        return ""
    u,v = test1(p)
    if test2(u)==0:
        return u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for j in u[1:len(u) - 1]:
            if j == '(':
                answer += ')'
            else:
                answer += '('
        return answer