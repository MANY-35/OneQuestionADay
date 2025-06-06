# LV2 더 맵게

### 1차시도 (실패)
```py
def solution(scoville, K):
    c = 0
    while len(scoville) >= 1:
        scoville.sort()
        a = b = 0
        for i in scoville:
            if i < K:
                a = scoville[0]
                b = scoville[1]
                break
        if a == b:
            if len(scoville) == 1:
                return -1
            return c

        scoville[1] = a + (2*b)
        scoville = scoville[1:]
        c += 1
```
런타임 에러와 성공, 실패가 섞여서 나왔다.

*****

### 2차시도 (실패)
```py
def solution(scoville, K):
    arr = [scoville[i] for i in range(len(scoville)) if scoville[i] < K]

    over = True if max(scoville) > K else False

    answer = 0
    while len(arr) > 1:
        t = [arr.pop(0) for i in range(2)]
        arr.append(t[0] + t[1]*2)
        arr.sort()
        answer += 1

    if over or min(arr) > K: 
        return answer
    return -1
```
런타임 에러는 잡았지만 몇몇 케이스와 효율성 테스트를 실패했다.

*****

#3차 시도 (실패)
```py
def solution(scoville, K):
    arr = [0 for i in range(K+1)]

    for s in scoville:
        if s >= K:
            arr[K] += 1
        else:
            arr[s] += 1

    num = [0,0]
    answer = c = 0
    l = len(arr)-1
    for i in range(l):
        if arr[i] > 0:
            num[c] = i
            arr[i] -= 1
            i -= 1
            c += 1

        if c == 2:
            t = num[0] + num[1]*2
            if t > K:
                arr[K] += 1
            else:
                arr[t] += 1
            c = 0
            answer += 1

    if arr[K] > 0 and arr[K-1] > 0:
        answer += 1

    if arr[K] == 0:
        return -1
    return answer
```
O(n)일거라고 생각했는데 오히려 일부 데이터 케이스에 시간초과가 나왔다.

*****

### 4차시도 (실패)
```py
def solution(scoville, K):
    m = max(scoville)*3 + 1
    if m <= K:
        return -1
    arr = [0 for i in range(max(scoville)*3 + 1)]

    for i in scoville:
        arr[i] += 1

    num = [0,0]
    answer = c = 0
    l = len(arr) - 1
    for i in range(l):
        if i >= K:
            break
        if arr[i] > 0:
            num[c] = i
            arr[i] -= 1
            i -= 1
            c += 1
        if c == 2:
            arr[num[0] + num[1]*2] += 1
            c = 0
            answer += 1
    return answer
```
시간 초과한 데이터 케이스는 없어졋다.  
K의 범위가 10억까지여서 이전 코드에서 시간초과가 발생 한 것 같아서 주어진 값에서 가장큰값의 3배만큼만 만들었는데 런타임 에러가 발생한 케이스가 있는 것으로 미루어보아 생각을 잘못 한 것 같다.

*****

### 5차시도 (실패)
```py
def solution(scoville:list, K):
    scoville.sort(reverse=True)
    i = 0
    while True:
        a = scoville.pop()
        b = scoville.pop()
        if a >= K and b >= K:
            break
        scoville.append(a + (b*2))
        scoville.sort(reverse=True)
        i += 1
        if scoville[-1] >= K or len(scoville) == 1:
            break
    if scoville[-1] < K:
        return -1
    return i
```
모든 데이터케이스는 성공했지만 효율성 테스트를 통과하지 못했다.
>도저히 효율성 테스트를 통과할만한 방법이 떠오르지 않아 힌트를 보니 heapq를 사용하지 않으면 풀수 없는것 같다.

### 6차시도 (성공)
```py
import heapq

def solution(scoville, K):
    scoville.sort()
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)
        answer += 1
    return answer
```
heapq 에 대해 공부를 좀더 해야 겠다.