from collections import deque

def dequeToString(str_list):
    result = ""
    for s in str_list:
        result += s
    return result
def L(n):
    n = deque(n)
    tmp = n.popleft()
    n.append(tmp)
    s = dequeToString(n)
    return s
def R(n):
    n = deque(n)
    tmp = n.pop()
    n.appendleft(tmp)
    s = dequeToString(n)
    return s
def D(n):
    n = int(n)
    if n*2 <=9999:
        n = n*2
    else:
        n = (n*2)%10000
    return str(n)
def S(n):
    n = int(n)
    n -= 1
    return str(n)

def Searching(n,searchTree):
    

T = int(input())
for i in range(T):
    result = []
    n,d = map(str,input().split())
    searchTree = [[1]*10 for i in range(10)]
    searchTree[0][0] = 0
    