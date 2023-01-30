# def solution(numbers):
#     answer = []
#     for number in numbers:
#         if number == 0:
#             answer.append(0)
#             continue
#         if number == 1:
#             answer.append(1)
#             continue
#         if number == 2:
#             answer.append(1)
#             continue
#         binaryNumber = ""
#         while number>0:
#             binaryNumber=str(number%2)+binaryNumber
#             number//=2
            
#         if len(binaryNumber)%2 == 0 :
#             binaryNumber1 = "0"+binaryNumber
            
#             tmp1 = list(binaryNumber1)
#             flag = False
#             point = 1
#             while point <= len(binaryNumber):
#                 if tmp1[point] == "0":
#                     flag = True
#                     break
#                 else:
#                     point += 2
#             if flag == False:
#                 answer.append(1)
#                 continue
#             else:
#                 answer.append(0)
#                 continue
#         else :
            
#             tmp = list(binaryNumber)
#             flag = False
#             point = 1
#             while point < len(binaryNumber):
#                 if tmp[point] == "0":
#                     answer.append(0)
#                     flag = True
#                     break
#                 else:
#                     point += 2
#             if flag == False:
#                 answer.append(1)
#                 continue
    
#     return answer


def solution(numbers):
    answer = []
    for number in numbers:
        binaryNumber = ""
        while number>0:
            binaryNumber=str(number%2)+binaryNumber
            number//=2
        print(binaryNumber)
    
    
    return answer




print(solution([7, 42, 5]))2
print(solution([63, 111, 95]))


'''
111   3  ->  101 
1111111   7  ->  1110111, 1011111, 1111101 
가능한 겅우 -> 0101010
111111111111111   15  ->  111111101111111, 101111111111111, 111011111111111, 111110111111111, 

'''
