# LV3 야근 지수

### 1차 시도 (실패)
```py
def solution(n, works):
    s = sum(works) - n
    if s < 0:
        return 0
    k = s // len(works) * len(works)
    arr = [s//len(works) for _ in range(len(works))]
    
    for i in range(s-k):
        arr[i] += 1
    return sum([i*i for i in arr])
```
> 3개의 데이터 케이스만 정답을 맞췄다. 모든 값을 균등하게 배분하는 것이 최솟값을 구하는 방법일 것 같아 작성해보았는데, 반례를 한번 찾아봐야 할 것 같다.

*****

### 2차 시도 (실패)
```py
def solution(n, works):
    arr = sorted(works, reverse=True)
    s = sum(works) - n
    if s < 0:
        return 0
    a, b = [], []
    for i in arr:
        if i > s//len(arr):
            a.append(i)
        else:
            b.append(i)
    s = sum(a) - n
    a = [s//len(a) for _ in range(len(a))]
    k = s // len(a) * len(a)
    for i in range(s-k):
        a[i] += 1    
    return sum([i*i for i in a] + [i*i for i in b])
```
> 이전 코드에서 작업량이 낮은 값에도 중간값으로 증가시키는 오류가 있어서, 작업량이 중간보다 큰 값들에 대해서만 중간값으로 바꿔주도록 코드를 수정했다. 하지만 이번에는 3개의 데이터 케이스가 실패했다.

*****

### 3차 시도 (성공)
```py
def solution(n, works):
    arr = sorted(works, reverse=True)
    s = sum(arr) - n
    if s < 0:
        return 0
    b = []
    while arr:
        s = sum(arr) - n
        t = []
        for i in arr:
            if i > s//len(arr):
                t.append(i)
            else:
                b.append(i)
        if arr == t:
            break
        arr = t
    a = [s//len(arr) for _ in range(len(arr))]
    for i in range(s % len(a)):
        a[i] += 1  
    return sum([i*i for i in a] + [i*i for i in b])
```
> 중간값을 구하는 과정에서 편차가 큰 경우(예: [1, 2, 55, 125])에는 여전히 중간값을 맞추기 위해 더해지는 값들이 생기기 때문에, 증가하는 값들을 제외한 중간값으로 감소하는 값들만을 저장하여 계산했다.

*****