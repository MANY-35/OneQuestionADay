# LV3 파괴되지 않은 건물

### 1차시도 (실패)
```py
def solution(board, skill):
    for t, r1, c1, r2, c2, d in skill:
        t = t*2 - 3
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += (t)*d

    answer = 0
    for i in board:
        for j in i:
            if j > 0:
                answer += 1
    return answer
```
정확성부분에서는 시간이 충분하여 다 성공했으나 당연하게도 효율성 부분에서 시간초과가 발생했다. 

*****

### 2차시도 (실패)
```py
def solution(board, skill):
    arr = [[0 for _ in range(len(board[i]))] for i in range(len(board))]
    for t, r1, c1, r2, c2, d in skill:
        t = t*2 - 3
        for i in range(r1, r2+1):
            arr[i][c1] += t*d
            if c2 < len(board[0])-1:
                arr[i][c2+1] -= t*d
    answer = 0
    for i in range(len(arr)):
        if arr[i][0] + board[i][0] > 0:
            answer += 1
        for j in range(1, len(arr[i])):
            arr[i][j] += arr[i][j-1]
            if arr[i][j] + board[i][j] > 0:
                answer+=1
    return answer
```
이전 O(n^3) 에서 O(2n^2)으로 줄였다고 생각 했으나 여전히 시간초과가 발생한다. O(n^2)까지 줄여야 될 것 같다.
> 도저히 방법이 생각나지 않아 검색을 통해 누적합 알고리즘을 참고하여 만들었다.

*****

### 3차시도 (성공)
```py
def solution(board, skill):
    arr = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for t, r1, c1, r2, c2, d in skill:
        t = t*2 - 3
        arr[r1][c1] += t*d
        arr[r2+1][c1] += t*-d
        arr[r1][c2+1] += t*-d
        arr[r2+1][c2+1] += t*d
    
    for i in range(1, len(arr)):
        arr[i][0] += arr[i-1][0]
    
    for i in range(1, len(arr[0])):
        arr[0][i] += arr[0][i-1]
    
    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] + arr[i][j] > 0:
                answer += 1
    return answer
```
이전 코드에서 누적합 알고리즘을 정확하게 이해하지 못하여 생긴 문제였다. 
~~누적합의 개념을 더 공부하여 해결했다.~~