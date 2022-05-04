info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
answer = []

infolist = []

for i in info:
    tmplist = i.split()
    tmpint = int(tmplist[4])
    tmplist[4] = tmpint
    for j in tmplist:
        infolist.append(j)


for k in query:
    score = int(k[-3:])
    k = k[0:-3]
    k = k.replace(" ","")
    klist = k.split('and')
    cnt = 0
    for l in range(4,len(infolist),5):
        if infolist[l]>=score:
            check = 0
            if klist[0]!='-' and infolist[l-4]!=klist[0]:
                check = 1
            if klist[1]!='-' and infolist[l-3]!=klist[1]:
                check = 1
            if klist[2]!='-' and infolist[l-2]!=klist[2]:
                check = 1
            if klist[3]!='-' and infolist[l-1]!=klist[3]:
                check = 1
            if check == 0:
                cnt+=1  
    answer.append(cnt)
            
print(answer)
    