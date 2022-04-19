def solution(s):
    if len(s) == 1 :
        answer = len(s)
        return answer
    answer = 10000
    for i in range(1,len(s)//2+1):
        tmp = s[:i]
        cnt = 1
        result = []
        for j in range(i,len(s),i):
            a = s[j:j+i]
            if tmp == a :
                cnt+=1
            else :
                result.append(cnt)
                result.append(tmp)
                tmp = a
                cnt = 1
        result.append(cnt)
        result.append(tmp)
        finalresult = []
        for k in range(len(result)):
            if result[k] != 1:
                finalresult.append(result[k])
        strr = ''.join(str(e) for e in finalresult)
        answer = min(len(strr),answer)
    return answer