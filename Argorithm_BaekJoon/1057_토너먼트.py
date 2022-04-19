# N,kim,im = map(int,input().split())
# kim-=1
# im-=1
# cnt=1
# while True:
#     if N%2==0:
#         if abs(kim-im)==1 :
#             tmp1 , tmp2 = max(kim,im) , min(kim,im)
#             if tmp1%2!=0 :
#                 print(cnt)
#                 break
#             else :
#                 kim = kim//2
#                 im = im//2
#                 N-=1
#                 N=N//2
#                 cnt+=1
#         else:
#             kim = kim//2
#             im = im//2
#             N-=1
#             N=N//2
#             cnt+=1
#     else:
#         if abs(kim-im)==1 :
#             tmp1 , tmp2 = max(kim,im) , min(kim,im)
#             if tmp1%2!=0 :
#                 print(cnt)
#                 break
#             else :
#                 kim = kim//2
#                 im = im//2
#                 N=N//2
#                 cnt+=1
#         else:
#             kim = kim//2
#             im = im//2
#             N=N//2
#             cnt+=1


n, kim, im = map(int, input().split())
count = 0
while kim != im:
    kim -= kim // 2
    im -= im // 2
    count += 1
print(count)