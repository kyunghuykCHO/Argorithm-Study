from itertools import product

def solution(users, emoticons):
    answer = []
    plusUser = 0
    totalCost = 0
    discountProducts = list(product([10,20,30,40], repeat = len(emoticons)))
    for discountProduct in discountProducts:
        tempPlusUser = 0
        tempTotalCost = 0
        for user in users:
            cost = 0
            for i in range(len(discountProduct)):
                if discountProduct[i] >= user[0]:
                    cost += emoticons[i] * (1 - (discountProduct[i]/100))
            if cost >= user[1]:
                tempPlusUser += 1
            else :
                tempTotalCost += cost

        if plusUser < tempPlusUser :
            plusUser = tempPlusUser
            totalCost = tempTotalCost
        elif plusUser == tempPlusUser and totalCost <= tempTotalCost :
            totalCost = tempTotalCost
        
    answer.append(plusUser)
    answer.append(totalCost)
    return(answer)

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))














