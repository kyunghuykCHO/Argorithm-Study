# A,B,V = map(int,input().split())
# tmp1 = V-A
# tmp2 = A-B
# if tmp1%tmp2==0:
#     print(tmp1+1)
# else:
#     tmp3=V//(A-B)
#     print(tmp3+1)

A, B, V = map(int, input().split())
 
high = V - A
if high % (A-B) == 0:
    first = int(high/(A-B))
else:
    first = int(high/(A-B) + 1)
print(first + 1)

