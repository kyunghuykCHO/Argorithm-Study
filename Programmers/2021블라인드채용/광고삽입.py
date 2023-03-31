def solution(play_time, adv_time, logs):    
    p = toSecond(play_time)
    a = toSecond(adv_time)
    viewers = [0 for _ in range(p+1)]

    for log in logs:
        start = toSecond(log[:8])
        end = toSecond(log[9:])
        viewers[start] += 1
        viewers[end] -= 1
        
    for i in range(1,len(viewers)):       
        viewers[i] += viewers[i-1]
        
    for i in range(1,len(viewers)):       
        viewers[i] += viewers[i-1]
        
    largest_view = viewers[a-1]             
    result = 0
    for i in range(a, p):
        if largest_view < viewers[i]-viewers[i-a]:
            largest_view = viewers[i]-viewers[i-a]
            result = i+1 - a
    result = toString(result) 
    return result


def toSecond(strr):
    h, m, s = strr.split(':')
    return 3600*int(h) + 60*int(m)+int(s)

def toString(num):
    h = str(num//3600)
    if len(h)==1:
        h = "0"+h
    m = str((num%3600) // 60)
    if len(m)==1:
        m = "0"+m
    s = str((num%3600)%60)
    if len(s)==1:
        s = "0"+s 
    answer = h+":"+m+":"+s
    return answer
