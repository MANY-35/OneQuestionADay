# LV2 지게차와 크레인

### 1차 시도 (실패)
```py
from collections import deque
def solution(storage, requests):
    answer = 0
    c = len(storage)
    r = len(storage[0])
    arr = [[0 for _ in range(r+2)] for _ in range(c+2)] 
    for i in range(c):
        for j in range(r):
            arr[1+i][j+1] = storage[i][j]
    for request in requests:
        temp = []
        if len(request) > 1:
            for i in range(1,c):
                for j in range(1,r):
                    if arr[i][j] == request[0]:
                        temp.append([i, j])
                        arr[i][j] = 1
                        answer+=1
            for i, j in temp:
                if finder(arr, i, j):
                    arr[i][j] = 0
        else:
            for i in range(1, c+1):
                for j in range(1, r+1):
                    if arr[i][j] == request[0]:
                        if finder(arr, i, j):
                            temp.append([i,j])
            for i, j in temp:
                arr[i][j] = 0
                answer+=1
    return r*c - answer

def finder(arr, c, r):
    vist = [[True for _ in range(len(arr[0]))] for _ in range(len(arr))]
    que = deque([[c, r]])
    while que:
        y, x = que.popleft()
        vist[y][x] = False
        for (i, j) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if arr[y+i][x+j] == 0:
                return True
            elif arr[y+i][x+j] == 1 and vist[y+i][x+j]:
                que.append([y+i, x+j])
    return False
```
해당 위치가 외각인지 아닌지 판단해 나아가면서 계산하는 코드를 작성해보았으나 절반 정도의 케이스에서 실패가 발생했고 몇 개의 케이스에서는 시간 초과가 발생했다.

*****

### 2차 시도 (성공)
```py
def solution(storage, requests):
    answer = 0
    arr = [[0 for _ in range(len(storage[0])+2)] for _ in range(len(storage)+2)] 
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            arr[1+i][1+j] = storage[i][j]
    
    for request in requests:
        vist = []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == request[0]:
                    if len(request) > 1:
                        arr[i][j] = 1
                    else:
                        if finder(arr, i, j):
                            vist.append((i,j))
        for y,x in vist:
            arr[y][x] = 0                
                
    for a in arr:
        for c in a:
            if c != 0 and c != 1:
                answer += 1
    return answer

def finder(arr, r, c):
    vist = set()
    que = [(r,c)]
    while que:
        y, x = que.pop()
        if x == 0 or x == len(arr[0]) or y == 0 or y == len(arr):
            continue
        vist.add((y,x))
        for i, j in [[1, 0], [0, 1], [-1,0], [0, -1]]:
            if arr[y+i][x+j] == 0:
                return True
            elif arr[y+i][x+j] == 1 and ((y+i),(x+j)) not in vist:
                que.append(((y+i),(x+j)))
    return False
```
너무 복잡하게 생각한 것 같다.  
크레인으로 빼는 경우만 1로 설정하고 finder 함수에서 길로 인식하도록 작성했으며, 지게차인 경우 해당 위치에서 현재 상황에서 뺄 수 있는 것들을 찾아내고 0으로 초기화해서 길의 종단부를 설정했다.