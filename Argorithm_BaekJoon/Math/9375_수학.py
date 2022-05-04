T = int(input())
for _ in range(T):
    n = int(input())
    
    clothes_type = {}
    for _ in range(n):
        name, type = input().split()
        if(type in clothes_type):
            clothes_type[type] += 1
        else:
            clothes_type[type] = 1
    
    case = 1
    for key in clothes_type.keys():
        case = case * (clothes_type[key] + 1)
    
    print(case - 1)