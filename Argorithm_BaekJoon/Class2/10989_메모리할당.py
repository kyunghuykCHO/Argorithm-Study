# # import sys
# # input = sys.stdin.readline

# # N = int(input())
# # numberlist = []
# # for i in range(N):
# #     numberlist.append(int(input()))
# # for j in sorted(numberlist):
# #     print(j)
# ##========== 내장함수 sort 메모리 초과 ==============

# # N = int(input())
# # numberlist = []
# # for i in range(N):
# #     numberlist.append(int(input()))

# # def quick_sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     pivot = arr[len(arr) // 2]
# #     lesser_arr, equal_arr, greater_arr = [], [], []
# #     for num in arr:
# #         if num < pivot:
# #             lesser_arr.append(num)
# #         elif num > pivot:
# #             greater_arr.append(num)
# #         else:
# #             equal_arr.append(num)
# #     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# # for j in quick_sort(numberlist):
# #     print(j)

# ##========== 퀵정렬 메모리 초과 ==============

# N = int(input())
# numberlist = []
# for i in range(N):
#     numberlist.append(int(input()))

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr

#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])

#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

# for j in merge_sort(numberlist):
#     print(j)

##========== 병합 정렬 메모리 초과 ==============

import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001
for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1
for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)