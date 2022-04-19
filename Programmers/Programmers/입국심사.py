# times = [6,8,10]
# tmptimes = []
# n = 10
# count = 0

# for i in times:
#     tmptimes.append(i)

# while count < n :
#     idx = times.index(min(times))
#     times[idx] += tmptimes[idx]
#     count+=1

# times[idx] -= tmptimes[idx]
# print(min(times))


def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        tested = 0
        mid = (left+ right) // 2
        for time in times:
            tested += mid // time
            if tested >= n:
                break
        
        if tested >= n:
            answer = mid
            right = mid - 1
        
        elif tested < n:
            left = mid + 1
            
    return answer