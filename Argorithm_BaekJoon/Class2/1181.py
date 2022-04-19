N = int(input())
WordsList=list()

for i in range(N):
    WordsList.append(input())

WordsList=sorted(WordsList, key=lambda x:(len(x), x))
resultList=[]
for i in WordsList :
    if i not in resultList:
        resultList.append(i)

for i in resultList:
    print(i)