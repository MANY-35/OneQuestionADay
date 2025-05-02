# LV2 [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지

### 1차 시도(실패)
```py
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
        
        if time <= limit:
            answer = target
            right = target
            target = (right+left) // 2
        else :
            left = target
            target = (right+left) // 2
    return answer
```
문제에서 구하고자 하는 값을 찾기 위해 이분 탐색을 이용하여 풀어보았다. 몇개의 테스트 케이스에서 실패했다. 

*****

### 2차 시도 (성공)
```py
def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    target = (right+left) // 2
    answer = 0

    while left <= target:
        time = 0
        for i in range(len(diffs)):
            time += times[i]
            if target < diffs[i]:
                time += (diffs[i] - target) * (times[i] + times[i-1])
        
        if time <= limit:
            answer = target
            right = target-1
            target = (right+left) // 2
        else :
            left = target+1
            target = (right+left) // 2   
    return answer
```
이진 탐색을 진행할 때 현재 값을 기준으로 새로운 값을 잡으면 모든 경우를 탐색하지 않는다는 것을 발견하고 이를 수정함.
