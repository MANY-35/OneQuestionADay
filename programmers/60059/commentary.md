# LV3 자물쇠와 열쇠

### 1차시도 (실패)
```py
def turn(arr):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            t[j][-1-i] = arr[i][j]
    return t

def move(arr, w):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    x, y = w
    for i in range(max(0, y), len(arr)+min(0, y)):
        for j in range(max(0, x), len(arr)+min(0, x)):
            t[i-y][j-x] = arr[i][j]
    return t

def checker(arr, answer):
    return all([arr[i][j] for i, j in answer])
    
def func(arr, answer, i,j, visted = []):
    if not any(list(map(any, arr))):        
        return False
    if checker(arr, answer):
        return True    
    
    for ii, jj in [(0,1), (1,0), (-1,0), (0,-1)]:
        if (i+ii, j+jj) not in visted:
            visted.append((i+ii, j+jj))
            t = move(arr, (ii, jj))
            if func(t, answer, i+ii, j+jj, visted):
                return True
    return False

def solution(key, lock):
    answer = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                answer.append((i, j))
    for i in range(4):
        if func(key, answer, 0, 0):
            return True
        key = turn(key)
    return False
```
> key배열을 회전과 이동을 통해 자물쇠 배열과 비교하는 방식으로 풀어보았는데 재귀함수를 사용해서 크기가 커지면 오류가 발생 할 것을 예상하긴 했으나 런타임 에러를 포함하여 실패한 케이스도 존재하는 것으로 미루어 보아 알고리즘 적으로 오류가 있는 것 같다.

*****

### 2차시도 (실패)
```py
def turn(arr):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            t[j][-1-i] = arr[i][j]
    return t

def check(arr, answer):
    c = []
    for i in range(len(answer)):
        c.append([])
        for j in range(len(answer)):
            c[-1].append(arr[i][j] + answer[i][j])
    for i in c:
        for j in i:
            if j != 1:
                return False
    return True 

def solution(key, lock):
    answer = [ (i,j) for i in range(len(lock)) for j in range(len(lock)) if lock[i][j] == 0]
    xs, xe = len(lock), 0
    ys, ye = len(lock), 0
    for y, x in answer:
        if xs > x:
            xs = x
        if xe < x:
            xe = x+1
        if ys > y:
            ys = y
        if ye < y:
            ye = y+1
    
    answer = []
    for i in range(ys, ye):
        answer.append([])
        for j in range(xs, xe):
            answer[-1].append(lock[i][j])

    for i in range(4):
        for y in range(len(key)-(ye-ys)+1):
            for x in range(len(key)-(xe-xs)+1):
                t = []
                for i in range(y, y+(ye-ys)):
                    t.append([])
                    for j in range(x, x+(xe-xs)):
                        t[-1].append(key[i][j])
                if check(t, answer):
                    return True
        key = turn(key)
    return False
```
> 자물쇠의 홈을 기준으로 열쇠를 슬라이싱 하여 맞는 모양이 있는지 판단하는 코드를 작성했다. 하나의 케이스에서 실패했으며 몇개의 케이스에서 런타임 에러가 발생했다. 런타임 에러는 배열의 범위에서 문제가 발생한 것 같다.

*****

### 3차시도 (실패)
```py
def turn(arr):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            t[j][-1-i] = arr[i][j]
    return t

def check(arr, answer):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            c = arr[i][j] + answer[i][j]
            if c == 2 or c==0:
                return False
    return True

def solution(key, lock):
    answer = [ (i,j) for i in range(len(lock)) for j in range(len(lock)) if lock[i][j] == 0]
    xs, xe = len(lock), 0
    ys, ye = len(lock), 0
    for y, x in answer:
        if xs > x:
            xs = x
        if xe < x:
            xe = x+1
        if ys > y:
            ys = y
        if ye < y:
            ye = y+1
    
    answer = []
    for i in range(ys, ye):
        answer.append([])
        for j in range(xs, xe):
            answer[-1].append(lock[i][j])
    
    for i in range(4):
        for y in range(len(key)-(ye-ys)+1):
            for x in range(len(key)-(xe-xs)+1):
                t = []
                for i in range(y, y+(ye-ys)):
                    t.append([])
                    for j in range(x, x+(xe-xs)):
                        t[-1].append(key[i][j])
                if check(t, answer):
                    return True
        key = turn(key)
    return False
```
> check 함수에서 정사각형만 검사하는 오류를 범했다.
> 풀이 과정에서 직사각형으로 슬라이스를 만들었는데 정 사각형으로 단정 지어버렸다. 하지만 1번케이스 하나를 실패했다.

*****

### 4차시도 (성공)
```py
def turn(arr):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            t[j][-1-i] = arr[i][j]
    return t

def check(arr, answer):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            c = arr[i][j] + answer[i][j]
            if c == 2 or c==0:
                return False
    return True

def solution(key, lock):
    answer = [ (i,j) for i in range(len(lock)) for j in range(len(lock)) if lock[i][j] == 0]
    xs, xe = len(lock), 0
    ys, ye = len(lock), 0
    for y, x in answer:
        if xs > x:
            xs = x
        if xe <= x:
            xe = x+1
        if ys > y:
            ys = y
        if ye <= y:
            ye = y+1
    
    answer = []
    for i in range(ys, ye):
        answer.append([])
        for j in range(xs, xe):
            answer[-1].append(lock[i][j])

    for i in range(4):
        for y in range(len(key)-(ye-ys)+1):
            for x in range(len(key)-(xe-xs)+1):
                t = []
                for i in range(y, y+(ye-ys)):
                    t.append([])
                    for j in range(x, x+(xe-xs)):
                        t[-1].append(key[i][j])
                if check(t, answer):
                    return True
        key = turn(key)
    return False
```
> lock에서 모든 구역에서 검사를 진행해야 할 때 범위를 정하는 부분에서 문제가 있다는 것을 발견하여 수정했다.