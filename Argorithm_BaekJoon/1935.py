number = int(input())
strlist = list(input())
diction = {}

for i in range(len(strlist)):
    if strlist[i].isalpha() :
        if strlist[i] in diction:
            strlist[i] = diction[strlist[i]]
        else:
            a = input()
            diction[strlist[i]] = a
            strlist[i] = a

stack = []
for j in strlist:
    if j.isdigit():
        stack.append(j)
    else:
        a=float(stack.pop())
        b=float(stack.pop())
        if j=='+':
            c = b+a
            stack.append(c)
        if j=='-':
            c = b-a
            stack.append(c)
        if j=='*':
            c = b*a
            stack.append(c)
        if j=='/':
            c = b/a
            stack.append(c)

result = stack.pop()
print("{:.2f}".format(result))