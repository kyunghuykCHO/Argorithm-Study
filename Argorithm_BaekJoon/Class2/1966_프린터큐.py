# from collections import deque
# T = int(input())
# for _ in range(T):
#     N,M = map(int,input().split())
#     doc = deque(map(int,input().split()))
#     target = doc[M]
#     n = doc.count(target)
#     if n==1:
#         doc = list(doc)
#         doc.sort(reverse=True)
#         print(doc.index(target)+1)
#     else:
#         cnt = 0
#         targetcnt = 0
#         while doc:
#             tmp = doc.popleft()
#             cnt+=1
#             for j in range(1,N):
#                 if doc[j]>tmp:
#                     if tmp == target:
#                         targetcnt+=1
#                     doc.append(tmp)
#                     cnt-=1
#                     break
#         print(cnt-targetcnt+1)
        

T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    doc = list(map(int,input().split()))
    imp = [0 for j in range(N)]
    imp[M] = 1
    cnt = 0
    while True:
        if doc[0] == max(doc):
            cnt+=1
            if imp[0] == 1:
                print(cnt)
                break
            else:
                del doc[0]
                del imp[0]
        else:
            doc.append(doc[0])
            del doc[0]
            imp.append(imp[0])
            del imp[0]
