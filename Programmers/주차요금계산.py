import math

def searching(parking,number,time):
    parkingTime = 0
    for i in parking:
        if i[0] == number and i[2] == "IN":
            parkingTime = time - i[1]
            i[2] = "OUT"
    return parkingTime


def solution(fees, records):
    basicTime = fees[0]
    basicFee = fees[1]
    unitTime = fees[2]
    unitFee = fees[3]
    
    answer = []
    parking = []
    parkingRecord = []
    for record in records:
        time,number,state = record.split(" ")
        hour,minutes = time.split(":")
        time = int(hour)*60 + int(minutes)
        if state == "IN":
            parking.append([number,time,state])
        elif state == "OUT":
            parkingTime = searching(parking,number,time)
            if number in parkingRecord:
                for ans in answer:
                    if ans[0]==number:
                        ans[1]+=parkingTime
            else:
                answer.append([number,parkingTime])
                parkingRecord.append(number)
            
    for p in parking:
        if p[2]=="IN":
            noOutNumber = p[0]
            lastedTime = 1439 - p[1]
            count = 0
            for ans in answer:
                if ans[0]==noOutNumber:
                    ans[1]+=lastedTime
                    break
                count += 1
            if count == len(answer):
                answer.append([noOutNumber,lastedTime])
    answer.sort()
    result = []
    for ans in answer:
        if ans[1] <= basicTime:
            result.append(basicFee)
        else:
            result.append(basicFee + math.ceil((ans[1] - basicTime) / unitTime) * unitFee)
    return result


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
