N = int(input())
grade = list(map(int,input().split()))
fixedgrade = []
standard = max(grade)
for i in grade:
    fixedgrade.append(i/standard*100)
result = sum(fixedgrade)/len(fixedgrade)
print(result)