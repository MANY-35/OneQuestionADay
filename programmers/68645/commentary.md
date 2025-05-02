# LV2 삼각 달팽이

### 1차시도 (실패)
```py
def solution(N):
    arr = [[] for j in range(N)]
    num = 1
    flag = 1
    swap = False
    y = -1
    for i in range(N):
        for j in range(N-i):
            y += flag
            if swap:
                t = arr[y].pop()
                arr[y].append(num)
                arr[y].append(t)
            else:
                arr[y].append(num)     
            num += 1
        flag -= 1
        if flag == -2:
            flag = 1
            swap = True
    
    answer = []
    for a in arr:
        for i in a:
            answer.append(i)
    return answer
```
N이 충분히 큰 삼각형에 대해서 뒤에서부터 한개만 바꾸는 것이 아니라 x개만큼 바꿔야 하는 것을 고려하지 않았다.

*****

### 2차시도 (실패)
```py
def solution(N):
    arr = [[0 for i in range(N)] for j in range(N)]
    x = 0
    y = -1
    xi = 0
    yi = num = 1

    for i in range(N):
        for j in range(N-i):
            y += yi
            x += xi
            arr[y][x] = num
            num += 1
        yi -= 1
        if yi < -1:
            yi = 1
        xi += 1
        if xi > 1:
            xi = -1
            
        answer = []
        for a in arr:
            for i in a:
                if i > 0:
                    answer.append(i)
    return answer
```
n*n배열에 직접 할당하는 방식으로 코드를 수정했는데 n이 크면 시간초과가 나오는 것 같다.

*****

### 3차시도 (실패)
```py
def solution(N):
    arr = [[] for j in range(N)]
    num = 1
    flag = 1
    swap = 0
    y = -1
    for i in range(N):
        for j in range(N-i):
            y += flag
            t = []
            for k in range(swap):
                t.append(arr[y].pop())
            arr[y].append(num)     
            for k in range(len(t)):
                arr[y].append(t.pop())
            num += 1
        flag -= 1
        if flag == -2:
            flag = 1
            swap += 1
    answer = []
    for a in arr:
        for i in a:
            answer.append(i)
    return answer
```
1차 코드에서 x개만큼을 바꾸는 코드를 추가했는데 충분히 큰 N에서 여전히 시간초과가 나온다.

*****

### 4차시도 (성공)
```py
def solution(N):
    arr = [[0]*j for j in range(1, N+1)]
    x = 0
    y = -1
    xi = 0
    yi = num = 1

    for i in range(N):
        for j in range(N-i):
            y += yi
            x += xi
            arr[y][x] = num
            num += 1
        yi -= 1
        if yi < -1:
            yi = 1
        xi += 1
        if xi > 1:
            xi = -1
    return sum(arr, [])
```
2차원배열을 1차원 배열로 변경하는 과정에서 많은 시간이 소모되는 것으로 판단하여 검색해보니 원소를 일일히 더하는 것이 아니라 배열자체를 더해가는 편이 더 빠르다는 것을 알았다.  
또한 그러기 위해서는 배열을 n*n이 아니라 처음부터 삼각형으로 선언하여 0을 거르는 불필요한 작업을 하지 않아도 되도록 수정했다.