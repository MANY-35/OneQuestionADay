# LV2 오픈 채팅방

### 1차 시도 (실패)
```py
def solution(m, n, board):
    arr = [[c for c in l] for l in board]

    while True:
        b = [] 
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != 0 and arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] :
                    b.append([i,j])
        if b == []:
            break

        for i, j in b:
            arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = 0

        for i in range(n):
            for j in range(m-1):
                for k in range(j, m):
                    if arr[k][i] == 0:
                        t = arr[k][i]
                        arr[k][i] = arr[j][i]
                        arr[j][i] = t

    answer = 0
    for i in arr:
        answer += i.count(0)
    return answer
```
> 데이터 케이스 3개가 실패했다. 예외 처리에서 문제가 발생한 것으로 보인다.

*****

### 2차 시도 (실패)
```py
def solution(m, n, board):
    arr = [[c for c in l] for l in board]

    while True:
        b = [] 
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != 0 and arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] :
                    b.append([i,j])
        if b == []:
            break

        for i, j in b:
            arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = 0

        for i in range(n):
            for j in range(m-1):
                if arr[j][i] == 0:
                    for k in range(j):
                        t = arr[k][i]
                        arr[k][i] = arr[j][i]
                        arr[j][i] = t

    answer = 0
    for i in arr:
        answer += i.count(0)
    return answer
```
> 이전 코드에서 정렬할 때 삽입 정렬을 해버려서 0과 첫 번째 값을 바꿔버리는 실수를 했다. 그래서 아래로 한 줄씩 내려주는 버블 정렬로 바꾸었지만 1개의 테스트 케이스를 실패했다.

*****

### 3차 시도 (성공)
```py
def solution(m, n, board):
    arr = [[c for c in l] for l in board]

    while True:
        b = [] 
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != 0 and arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] :
                    b.append([i,j])
        if b == []:
            break

        for i, j in b:
            arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = 0

        for i in range(n):
            for j in range(m):
                if arr[j][i] == 0:
                    for k in range(j):
                        t = arr[k][i]
                        arr[k][i] = arr[j][i]
                        arr[j][i] = t

    answer = 0
    for i in arr:
        answer += i.count(0)
    return answer
```
> 1차 시도에서 2차 시도로 바꿀 때 정렬 방식을 바꾸면서 전체 범위를 m-1에서 m으로 바꾸는 것을 깜빡했다. 코드를 변경한 후 한 번 더 범위를 검사하는 습관을 가져야 할 것 같다.