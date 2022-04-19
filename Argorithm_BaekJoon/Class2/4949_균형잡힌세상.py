# lines = []
# while True:
#     line = input()
#     if line == ".":
#         break
#     lines.append(line)

# for line in lines:
#     smallstack = []
#     bigstack = []
#     teststack = []
#     for j in line:
#         if j==".":
#             print("yes")
#             break
#         if j == "(":
#             teststack.append(j)
#         elif j == ")":
#             if len(teststack)==0:
#                 print("no")
#                 break
#             else:
#                 tmp = teststack.pop()
#             if tmp != "(":
#                 print("no")
#                 teststack.append(tmp)
#                 break
#             teststack.pop()
#         if j == "[":
#             teststack.append(j)
#         elif j == "]":
#             if len(teststack)==0 :
#                 print("no")
#                 break
#             else:
#                 tmp = teststack.pop()
#             if tmp != "[":
#                 print("no")
#                 teststack.append(tmp)
#                 break
#             teststack.pop()
    

while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()
    if temp == True and not stk:
        print('yes')
    else:
        print('no')