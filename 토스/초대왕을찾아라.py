# 프로그래머스 칫솔판매다단계 확인 
# 트리문제 

invitement = [[1,2],[2,3],[2,4],[2,5],[5,6],[5,7],[6,8],[2,9]]
ans = {}
dic = {}
for i in range(len(invitement)):
    dic[invitement[i][0]] = list()

for i in range(len(invitement)):
    dic[invitement[i][0]].append(invitement[i][1])

for i in dic.keys():
    if dic[i]:
        length = len(dic[i])
        ans[i] = length*10
        for j in dic[i]:
            if j in dic:
                length = len(dic[j])
                ans[i] = ans[i] + length*3
                for k in dic[j]:
                    if k in dic:
                        length = len(dic[k])
                        ans[i] = ans[i] + length
print(ans)