import math

def solution(n, k):
    if k==10:
        num = str(n)
    else:
        num = str(decimalToN(n, k))
    answer = 0
    i=0
    p = ""
    while i<len(num):
        if num[i] != "0" :
            p += num[i]
            i+=1
        else :
            if p !="" and is_prime_number(int(p)) == True:
                answer +=1
                p = ""
                i+=1
            else:
                p = ""
                i+=1
    if p!="" and int(p)>0 and is_prime_number(int(p)) == True:
        answer+=1
    return answer
        
def decimalToN(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1] 
    
def is_prime_number(p):
    if p==1:
        return False
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False 
    return True 


print(solution(36,3))

