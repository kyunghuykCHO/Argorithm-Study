import math

N = int(input())
result = 0
if N==1:
    result = 3
elif N==2 :
    result = 9
elif N==3 :
    result = 26
# elif N==4 :
#     result = 76
else :
    cnt = 0
    for i in range(3,N-1):
        # 왼쪽 끝
        cnt += math.pow(3,N-i-1)*2
    
        # 오른쪽 끝
        cnt += math.pow(3,N-i-1)*2
    
        # 가운데
        cnt += (math.pow(3,N-i-2)*2*2)*(N-i-1)
    
    # N-1 일 때
    cnt+=4
    
    # 꽉참
    cnt += 1
    result = (math.pow(3,N) - cnt)
        
print(result%1000000007)