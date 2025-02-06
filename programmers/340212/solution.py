
def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    target = right//2
    answer = 0

    while left < target:
        time = 0
        for i in range(len(diffs)):
            time += times[i]
            if target < diffs[i]:
                time += (diffs[i] - target) * (times[i] + times[i-1])
        print(time, target,"|", left, ":", right)
        
        if time <= limit:
            answer = target
            right = target
            target = (right+left) // 2
        else :
            left = target
            target = (right+left) // 2
        
    return answer


print(solution([1, 14, 1], [1, 7, 1], 30))