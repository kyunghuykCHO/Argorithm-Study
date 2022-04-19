a,b = map(str,input().split())

a_list = list(a)
a_list.reverse()
a = ''.join(a_list)
a = int(a)
b_list = list(b)
b_list.reverse()
b = ''.join(b_list)
b = int(b)

if a>b:
    print(a)
else :
    print(b)