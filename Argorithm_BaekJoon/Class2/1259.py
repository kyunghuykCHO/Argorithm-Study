# inputlist = []

# while True:
#     a=input()
#     if(a=="0"):
#         break
#     else:
#         inputlist.append(a)

# for number in inputlist:
#     j=0
#     a = int(len(number)/2)-1
#     while True:

#         if number[j]!=number[len(number)-j-1]:
#             print("no")
#             break
#         elif j==a:  
#             print("yes")
#             break
#         else:
#             j+=1

while True: # 슬라이싱 
    n = input()

    if n =='0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')