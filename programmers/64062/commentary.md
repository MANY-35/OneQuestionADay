# LV3 징검다리 건너기

### 1차시도 (실패)
```py
def solution(stones, k):
    arr = []
    for i in range(len(stones)-k+1):
        flag = True
        for j in range(1, k):
            if stones[i+j] > stones[i]:
                flag = False
                break
        if flag:
            arr.append(stones[i])
    return min(arr)
```
절반 이상의 테스트에서 실패했다.  
k개 연속되는 징검 다리중 감소하는 값들의 리스트를 뽑고 그중 가장 작은 값을 구하는 방식으로 했는데 문제를 잘 못 해석한 것 같다.

*****

### 2차시도 (실패)
```py
def solution(stones, k):
    arr = []
    for i in range(0, len(stones)-k+1, k):
        max = stones[i]
        for j in range(1, k):
            if i+j >= len(stones):
                break
            if max < stones[i+j]:
                max = stones[i+j]
        arr.append(max)
    return min(arr)
```
이전보다 많은 케이스에서 성공했으나 여전히 실패한 케이스가 존재함

*****

### 3차시도 (실패)
```py
def solution(stones, k):
    arr = []
    i = 0
    while i<len(stones)-k+1:
        max = stones[i]
        mj = 0
        for j in range(k):
            if i+j >= len(stones):
                break
            if max < stones[i+j]:
                max = stones[i+j]
                mj = j
        arr.append(max)
        i+=mj+1
    return min(arr)
```
효율성 테스트에서 하나의 케이스가 실패했다.

******

### 4차시도 (실패)
```py
from collections import deque
def solution(stones, k):
    arr = deque([0])
    i = j = 0
    answer = 200000001
    while i<len(stones):
        
        if arr[0] < stones[i]:
            arr = deque([stones[i]])
        elif arr[-1] <stones[i]:
            arr.pop()
            arr.append(stones[i])
        else:
            arr.append(stones[i])
        j += 1
        if j == k or i == len(stones)-1:
            answer = min(answer, arr[0])
            j = len(arr)-1
            arr.popleft()
            if len(arr) < 1:
                arr = deque([0])
        i+=1 
    return answer
```
이전 코드는 중간중간 검사할 때 겹치는 부분이 생겨서 그 부분도 없애서 O(n)까지 줄여보려 했지만 절반정도 케이스에서 실패했다.  
알고리즘 적으로 생각해봐야 할 것 같다.

*****

### 5차시도 (실패)
```py
from collections import deque
def solution(stones, k):
    arr = deque([])
    i = j = c = 0
    answer = 2000000000
    while i<len(stones):
        if len(arr) < 1:
            arr.append(stones[i])
        elif arr[0] <= stones[i]:
            arr = deque([stones[i]])
            c = 0
        else:
            while arr[-1] < stones[i]: 
                arr.pop()
                c+=1
            arr.append(stones[i])
        j += 1
        if j >= k:
            answer = min(answer, arr[0])
            j = len(arr)+c-1
            c = 0
            arr.popleft()
        i+=1 
    return answer
```
절반 이상의 데이터케이스에서 성공했으나 여전히 실패한 케이스가 존재한다.  
어떤 부분을 잘 못하고 있는지 찾는것이 알려진 케이스가 너무 적어서 쉽지않다.

*****

### 6차시도 (성공)
```py
from collections import deque
def solution(stones, k):
    if k == 1:
        return min(stones)
    arr = deque([])
    answer = 200000001
    for i, s in enumerate(stones):
        if len(arr)<1:
            arr.append([i,s])
        else:
            while arr:
                if arr[-1][1] < s:
                    arr.pop()
                else:
                    break
            arr.append([i,s])
        if i < k-1:
            continue
        if arr[0][0] < i-k+1:
            arr.popleft()   
        answer = min(answer, arr[0][1])    
    return answer
```
도저히 감이 잡히지 않아 다른사람의 힌트를 참고하여 작성했다.  
작성한 코드와 거의 비슷한것 같은데 차이점을 분석해봐야 겠다.