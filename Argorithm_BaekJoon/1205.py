
N, score, P = map(int,input().split())
count=0
rank=0
RankingList=[]

if N>0 :
    ScoreList = list(map(int,input().split()))
    ScoreList.sort()
    ScoreList.reverse()
    if(N==P and ScoreList.pop()>=score):
        print(-1)
        exit()  
    ScoreList.append(score)
    ScoreList.sort()
    ScoreList.reverse()

    for i in range(len(ScoreList)):
        if i==0:
            RankingList.append(1)
        else:
            if ScoreList[i]==ScoreList[i-1] :
                RankingList.append(RankingList[i-1])
            else:
                RankingList.append(i+1)

elif N==0:
    print(1)
    exit()

index = ScoreList.index(score)
print(RankingList[index])