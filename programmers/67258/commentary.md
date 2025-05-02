# LV3 보석 쇼핑

### 1차시도 (실패)
```py
def solution(gems):
    left = right = len(gems) - 1
    answer = []
    check = [gems[right]]
    l = len(set(gems))
    if l < 2:
        return [1, 1]
    while left > 0:
        left -= 1
        if gems[left] == gems[right]:
            right -= 1
        
        if gems[left] not in check:
            check.append(gems[left])
        if len(check) == l:
            answer.append([left+1, right+1])
            left = right-1
            check = [gems[left]]
    return sorted(answer, key= lambda x:(x[1]-x[0], x[0]))[0]
```
시간이 너무 걸려서 시간초과가 발생했다.

*****

### 2차시도 (실패)
```py
def solution(gems):
    check = l = len(set(gems))
    while l <= len(gems):
        for i in range(len(gems)-l+1):
            if check == len(set(gems[i:i+l])):
                return [i+1, i+l]
        l+=1
```
간단하게 풀어보려했는데 역시 시간 초과가 발생했다. 

*****

### 3차시도 (실패)
```py
from collections import deque
def solution(gems):
    check = set(gems)
    left, right = 0, len(set(gems))
    arr = deque(gems[left:right])
    if set(arr) == check:
        return [1, len(arr)]
    answer = []
    while right < len(gems):
        arr.append(gems[right])
        while left < right:
            t = arr.popleft()
            if t not in arr:
                arr.appendleft(t)
                break
            left += 1
        if set(arr) == check:
            if len(arr) == len(check):
                return [left+1, right +1]
            answer.append([left+1, right+1])
            left = right - len(check) + 1
            arr = deque(gems[left:right+1])
        right += 1
    return sorted(answer, key=lambda x:x[1]-x[0])[0]
```
몇개의 케이스에서 실패했으며 효율성테스트 또환 시간초과가 대다수 발생했다.

*****

### 4차시도 (실패)
```py
from collections import deque
def solution(gems):
    check = set(gems)
    left, right = 0, len(set(gems))
    arr = deque(gems[left:right])
    if set(arr) == check:
        return [1, len(arr)]
    
    answer = []
    while right < len(gems):
        arr.append(gems[right])

        while left < right:
            t = arr.popleft()
            if t not in arr:
                arr.appendleft(t)
                break
            left += 1
        
        if set(arr) == check:
            answer.append([left+1, right+1])
        right += 1
    return sorted(answer, key=lambda x:x[1]-x[0])[0]
```
이전 코드에서의 오류를 보안하여 모든 케이스에서 성공했지만 여전히 시간이 부족함

*****

### 5차시도 (실패)
```py
def solution(gems):
    dc = {gem:0 for gem in gems}
    left = right = 0
    answer = [0, len(gems)]
    check = set()
    
    while right < len(gems):
        dc[gems[right]] += 1
        check.add(gems[right])
        while dc[gems[left]] > 1:
            dc[gems[left]] -= 1
            left += 1
        if check == dc.keys():
            if answer[1] - answer[0] > right - left:
                answer = [left, right]
        right += 1
    return [answer[0]+1, answer[1]+1]
```
dict 와 set을 이용해 시간을 줄여보았는데 단 3개의 케이스에서 시간초과가 발생했다.

*****

### 6차시도 (성공)
```py
def solution(gems):
    dc = {gem:0 for gem in gems}
    left = right = 0
    answer = [0, len(gems)]
    check = set()
    while right < len(gems):
        dc[gems[right]] += 1
        check.add(gems[right])
        if check == dc.keys():
            while dc[gems[left]] > 1:
                dc[gems[left]] -= 1
                left += 1
            if answer[1] - answer[0] > right - left:
                answer = [left, right]
            dc[gems[left]]  -= 1
            check.remove(gems[left])
            left += 1   
        right += 1
    return [answer[0]+1, answer[1]+1]
```
이전코드에서 check를 검사하는 방식을 바꿔서 불필요한 검사 시간을 줄였다.