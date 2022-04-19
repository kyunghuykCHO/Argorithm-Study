# W = 방수 H = 층 N = 몇번째 손님
TestCase = int(input())
for i in range(TestCase):
    H,W,N = map(int,input().split())
    YY = str(N%H)
    XX = str(N//H+1)
    if N%H==0 :
        YY = str(H)
        XX = str(N//H)

    print("{}{}".format(YY,XX.zfill(2)))