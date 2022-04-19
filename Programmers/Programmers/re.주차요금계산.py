# import math
# def solution(fees, records):
#     answer = []
#     ntime = fees[0]
#     ncost = fees[1]
#     ptime = fees[2]
#     pcost = fees[3]
#     cars = []
#     parkingrecord = []
#     answer = []
#     for record in records:
#         time,num,state = map(str, record.split())
#         a,b = map(int,time.split(":"))
#         time = a*60 + b
#         if state == "IN":
#             cars.append([num,time])
#         elif state == "OUT":
#             for i in cars:
#                 if i[0]==num:
#                     intime = i[1]
#                     i[0] = "출차됨"
#                     parkingtime = time - intime
#             flag = 0
#             for j in parkingrecord:
#                 if j[0] == num:
#                     j[1] += parkingtime
#                     flag=1
#             if flag==0:
#                 parkingrecord.append([num,parkingtime])
#     count=0  
#     for l in cars:
#         statingnum = l[0]
#         if statingnum == "출차됨":
#             continue
#         intime = l[1]
#         statetime = (60*23 + 59) - l[1]
#         for m in parkingrecord:
#             if m[0] == statingnum:
#                 m[1] += statetime
#                 count+=1
#         if count == 0 :
#             parkingrecord.append([statingnum,statetime])
#     parkingrecord.sort(key=lambda x: x[0])  
#     for k in parkingrecord:
#         if k[1]<=ntime:
#             answer.append(ncost)
#         else:
#             totalcost = ncost + (   math.ceil((k[1]-ntime)/ptime)   )*pcost
#             answer.append(totalcost)
#     return answer

# print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))


