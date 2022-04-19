while True:
    numlist = list(map(int,input().split()))
    numlist.sort()
    if numlist[0]==0:
        break
    else:
        if numlist[2]**2 == numlist[1]**2 + numlist[0]**2:
            print("right")
        else:
            print("wrong")