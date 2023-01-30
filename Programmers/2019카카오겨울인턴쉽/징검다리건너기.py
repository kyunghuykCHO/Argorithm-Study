def solution(stones, k):
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
                if count ==k :
                    break
            else:
                count = 0
        if count == k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left