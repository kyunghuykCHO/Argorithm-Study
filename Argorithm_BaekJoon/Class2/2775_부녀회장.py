T = int(input())
for i in range(T):
    K = int(input()) # 1 층 
    N = int(input()) # 3

    floor = []
    for j in range(1,N+1):
        floor.append(j)
    
    for k in range(K-1):
        #tmplist = floor # 주소복사 됨.. --> 복사 다시 얕은복사 깊은복사.. 공부 다시.. 
        tmplist = []
        for _ in floor:
            tmplist.append(_)
        print(tmplist)    
        for l in range(0,N):
            print("{} 는 l 입니다".format(l))
            result = 0
            for m in range(0,l+1):
                result += tmplist[m]
                print("{} 는 m 이고 {} 은 tmplist[{}] 입니다".format(m,tmplist[m],m))
            floor[l] = result
    
    print(floor)


# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력