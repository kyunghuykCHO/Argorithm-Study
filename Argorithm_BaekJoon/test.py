# 문자열 나누기
str = "abcd,efgh ijkl/mnop"
strList = str.split(",")

# 리스트 -> 변수 할당
l = [1,2,3]
a,b,c = l

# 문자열의 특정 위치 뽑아내기
s = "ksjdfnjkasdhbfs"
s = s[1:len(s)-3]

# 문자열 양 끝 제거
tmp = "ksjdfnjkasdhbfs"
tmp = tmp.lstrip("}")
tmp = tmp.rstrip("{")

# 리스트를 문자열로
arr = ["a","b","c","d"]
str = ''.join(arr)

# map - 리스트 수정 
answer = ["1","2","3"]
answer = list(map(int, tmp))

# 문자열 요소 제거
answer = ["1","2","3"]
answer.remove("1")

# 힙큐
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heapify(heap)
result = heapq.heappop(heap)
result2 = heap[0]
heap_items = [1,3,5,7,9]
max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))
print(max_heap)





# 약수 구하기 
def get_divisor(n):
    front = []
    back = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            front.append(i)
            if i != n // i:
                back.append(n // i)
    return front + back[::-1]


print(get_divisor(8))