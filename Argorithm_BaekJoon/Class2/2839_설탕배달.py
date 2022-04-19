# n = int(input())
# ans = 0
# a, b = divmod(n, 5)
# c = 0
# d = 0
# while True:
#     if b!=0:
#         c, d = divmod(b, 3)
#     if d==0:
#         ans = a + c
#         break
#     else:
#         a -= 1
#         b += 5
#     if a<0:
#         ans = -1
#         break
# print(ans)





N = int(input())
numberof5 = N//5
modofN = N%5
while True:

    if numberof5 ==0 and N%3 != 0 :
        print(-1)
        break

    numberof3 = modofN//3
    if modofN%3 == 0:
        print(numberof5+numberof3)
        break
    else:
        if numberof5>0:
            numberof5-=1
            modofN+=5
    