import itertools
def solution(orders, course):
    result = []
    answer=[]
    orderlist = []
    for order in orders:
        strlist = list(order)
        for str in strlist:
            orderlist.append(str)
    orderlist = list(set(orderlist))
    orderlist.sort()
    for c in course:
        nCr = itertools.combinations(orderlist, c)
        coms = list(nCr)
        L = []
        for i in range(len(coms)):
            L.append(0)
        for com in coms:
            for o in orders:
                check = 0
                for i in range(c):
                    if com[i] in o:
                        check+=1
                if check==c:
                    L[coms.index(com)]+=1
        m = max(L)
        if m>1:
            for i in range(len(L)):
                if L[i] == m:
                    result.append(coms[i])
    for r in result:
        answer.append(''.join(r))
    answer.sort()
    print(answer)

# 손님들의 주문한 메뉴로만 course set combinations
        
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        array = []
        for order in orders:
            # 주문 문자열 정렬
            order = sorted(order) 
            # array에 현재 주문에서 num개를 뽑아 나올 수 있는 경우를 넣음
            array.extend(list(combinations(order, num)))
        # 카운터를 사용하여 중복되는 횟수를 셈
        count = Counter(array)
        
        if count:
            # 제일 많이 나온 조합이 두번 이상 시켜졌다면
            if max(count.values()) >= 2:
                for key, value in count.items():
                    # 현재 조합이 가장 많이 시켜졌다면 결과배열에 추가
                    if value == max(count.values()):
                        answer.append("".join(key))
    
    # 정렬하여 return 
    return sorted(answer)
        
        
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])