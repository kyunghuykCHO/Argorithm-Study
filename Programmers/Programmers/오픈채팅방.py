def solution(record):
    answer = []
    
    ID = {}
    for i in record:
        tmp=list(i.split(" "))
        if tmp[0]=="Enter":
            ID[tmp[1]]=tmp[2]
        if tmp[0]=="Change":
            ID[tmp[1]]=tmp[2]
    
    for j in record:
        tmp2=list(j.split(" "))
        if tmp2[0]=="Enter":
            answer.append("{}님이 들어왔습니다.".format(ID.get(tmp2[1])))
        if tmp2[0]=="Leave":
            answer.append("{}님이 나갔습니다.".format(ID.get(tmp2[1])))
    
    return answer