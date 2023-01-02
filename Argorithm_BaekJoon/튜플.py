def solution(s):
    answer = [] 
    sList = s.split("},{")
        
    for i in range(len(sList)):
        tmp = sList[i]
        tmp = tmp.lstrip("{")
        tmp = tmp.rstrip("}")
        sList[i] = tmp
    
    sList.sort(key=len)
    
    removeList = []
    
    for s in sList:
        if len(s)==1:
            removeTarget = int(s)
            removeList.append(removeTarget)
            answer.append(removeTarget)
        else:
            tmpList = s.split(",")
            tmpList = list(map(int, tmpList))
            for removeTarget in removeList:
                tmpList.remove(removeTarget)
            answer.append(tmpList[0])
            removeList.append(tmpList[0])
    
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))