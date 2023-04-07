from collections import defaultdict

# 초기화 작업 
N = int(input())
dic = defaultdict(list)
for _ in range(N):
    root, leftNode, rightNode = map(str, input().split())
    if leftNode != ".": dic[root].append(leftNode)
    else: dic[root].append("null")
    if rightNode != ".": dic[root].append(rightNode)
    else: dic[root].append("null")

# 전위 순회
def preOrderTraverse(currentNode):
    global answer
    answer += currentNode
    if dic[currentNode] :
        nextNodeList = dic[currentNode]
        for nd in nextNodeList:
            if nd != "null" :
                preOrderTraverse(nd)
                
    # 이 부분을 좀 이쁘게 다시 짤 수 없나..?
    if currentNode == "A":
        return answer
    

# # 중위 순회
def inOrderTraverse(currentNode):
    global answer
    if dic[currentNode][0] != "null" : inOrderTraverse(dic[currentNode][0])
    answer += currentNode
    if dic[currentNode][1] != "null" : inOrderTraverse(dic[currentNode][1])
    if len(answer)==N:
        return answer


# # 후위 순회
def postOrderTraverse(currentNode):
    global answer
    if dic[currentNode][0] != "null" : postOrderTraverse(dic[currentNode][0])
    if dic[currentNode][1] != "null" : postOrderTraverse(dic[currentNode][1])
    answer += currentNode
    if len(answer)==N:
        return answer


answer = ""
print(preOrderTraverse("A"))

answer = ""
print(inOrderTraverse("A"))

answer = ""
print(postOrderTraverse("A"))