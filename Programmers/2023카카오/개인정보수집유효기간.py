# 광과삽입과 유형 비슷 

def solution(today, terms, privacies):
    answer = []
    termDict={}
    year, month, day=map(int, today.split('.'))
    
    for term in terms:
        term, period=term.split()
        termDict[term]=int(period)
    
    for i in range(len(privacies)):
        date, contractTerm=privacies[i].split()
        contractYear, contractMonth, contractDay=map(int, date.split('.'))
        
        contractMonth+=termDict[contractTerm]
        
        while contractMonth>12:
            contractMonth-=12
            contractYear+=1
        
        if contractYear>year:
            continue

        elif contractYear==year:
            if contractMonth>month:
                continue
                
            elif contractMonth==month:
                if contractDay>day:
                    continue
                    
        answer.append(i+1)
        
    return answer


print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))