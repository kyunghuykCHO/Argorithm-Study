# def distribution(sender, amt, dic, enroll,answer):
#     receiver = dic[sender]
#     # 딕셔너리로 referral 을 불러옴
#     if amt >= 10 and receiver != "-":
#     # receiver(= referral) 이 "-" 이 아닐 시
        # idx = enroll.index(receiver)
#         answer[idx] += (amt-int(amt*0.1))
#         distribution(receiver, int(amt*0.1),dic,enroll,answer)
#         return
#         # distribution 재귀
#     elif amt<10 and receiver != "-":
#         idx = enroll.index(receiver)
#         answer[idx] += amt
#         return
        
# def solution(enroll, referral, seller, amount):
#     for i in range(len(amount)):
#         amount[i] = amount[i]*100
#     answer = [0]*len(enroll)
#     # answer 배열 생성
#     dic = {}
#     for i in range(len(enroll)):
#         dic[enroll[i]] = referral[i]
#     # 딕셔너리를 이용해 referral 연결
#     for i in range(len(seller)):
#         idx = enroll.index(seller[i])
#     # seller 에서 하나씩 뽑아와서
#         if amount[i] >= 10:
#         # 만약 수입이 10보다 크다면 
#             answer[idx] += (amount[i] - int(amount[i]*0.1))
#             # answer의 맞는 index에 0.9 amount 추가
#             distribution(seller[i],int(amount[i]*0.1),dic,enroll,answer)
#             # 0.1 amount 만큼 distribution
#         else:
#             answer[idx] += amount[i]
#             # amount 가 10보다 작을 시 distribution 안함
    
#     return answer



# .index() 는 사용을 지양한다 --> 대신 딕셔너리를 두개를 사용한다. 
def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}
    for i in range(len(enroll)):
        dic[enroll[i]] = referral[i]
    money = {}
    for i in enroll:
        money[i] = 0
    for i in range(len(seller)):
        amt = amount[i]*100
        name = seller[i]
        while name != "-" and amt>0:
            money[name] += (amt - amt//10)
            amt = amt//10
            name = dic[name]
    for v in money.values():
        answer.append(v)
    return answer
        
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])
