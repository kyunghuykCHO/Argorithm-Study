T = int(input())
for i in range(T):
    line = input()
    stk = []
    temp = True
    for i in line:
        if i == '(':
            stk.append(i)
        elif i == ')':
            if not stk :
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
    if temp == True and not stk:
        print('YES')
    else:
        print('NO')