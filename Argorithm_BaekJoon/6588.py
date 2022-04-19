# numberlist=[]

# def find_prime(a):
#     primelist=[]
#     for i in range(a-1):
#         primelist.append(True)
#     x=len(primelist)

#     for i in range(0,x-1):
#         for j in range(i+1,x):
#             if primelist[j]==False:
#                 continue
#             elif primelist[j]==True and (j+2)%(i+2)==0:
#                 primelist[j]=False
#     print_primesum(a, primelist)

# def print_primesum(a, b):
#     for i in range(0,len(b)-1):
#         for j in range(i+1,len(b)):
#             if b[j]==True and i+j+4==a:
#                 print ("{}={} + {}".format(a,(i+2),(j+2)))
#                 return 0
#             else:
#                 continue



# while True:
#     num = int(input())
#     if num==0:
#         break
#     numberlist.append(num)
# for i in numberlist:
#         find_prime(i)



from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())

    if n == 0: break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break