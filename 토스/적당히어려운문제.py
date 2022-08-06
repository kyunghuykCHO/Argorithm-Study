levels = [2,4214,235,45,436,547,457,54765,765,74,364,5,4356,5465,756,8,458,65,754,6,43,56]
levels.sort(reverse=True)
flag = len(levels)//4
if len(levels)<=3:
    print(-1)
else:
    print(levels[flag])

