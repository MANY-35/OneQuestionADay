# LV2 N-Queen

### 1차시도 (실패)
```py
import copy
def dfs(poss, n, row, count):
    if row == n:
        return True
    if True not in poss[row]:
        return False
    for i in range(n):
        if poss[row][i]:
            temp = copy.deepcopy(poss)
            poss[row][i] = 'Q'
            for j in range(1,n):
                poss[(row+j)%n][i] = False
                if row+j < n and i+j < n:
                    poss[row+j][i+j] = False 
                if row+j < n and i-j >= 0:
                    poss[row+j][i-j] = False
                if row-j >= 0 and i+j < n:
                    poss[row-j][i+j] = False
                if row-j >= 0 and i-j >= 0:
                    poss[row-j][i-j] = False
            if dfs(poss, n, row+1, count):
                count[0] += 1
            poss = temp
            
def solution(n):
    poss = [[True] * n for _ in range(n)]
    answer = [0]
    dfs(poss, n, 0, answer)    
    return answer.pop()
```

모든 행에 대하여 하나의 행에는 하나의 퀸만 존재 할 수 있다는 점에서 착안하여 각행에 퀸을 배치할 수 있는 모든 경우의 수를 계산하는 방식으로 접근했다.  
n의 최대 값이 12이기 때문에 완전 탐색을 진행해도 시간이 충분할 줄 알았으나 두개의 케이스에서 시간초과가 발생했다.


*****

### 2차시도 (실패)
```py
def dfs(indexes, n, row, count):
    if row == n:
        count[0] += 1
        return
    
    arr = [True for _ in range(n)]
    for i in range(n):
        for r, c in indexes:
            arr[c] = False
            if abs(row-r) == abs(c-i):
                arr[i] = False
    for i in range(len(arr)):
        if arr[i]:
            indexes.append((row, i))
            dfs(indexes, n, row+1, count)
            indexes.pop()                
def solution(n):
    poss = []
    answer = [0]
    dfs(poss, n, 0, answer)    
    return answer.pop()
```
시간을 줄이기 위해 퀸의 위치 좌표만 가지고 현재 놓을 수 있는 퀸의 좌표들을 구별하는 방식으로 접근했으나 역시 마지막 n이 12일때 시간초과가 발생한다.

*****

### 3차시도 (성공)
```py
def dfs(indexes, n, row, count):
    if row == n:
        count[0] += 1
        return
    arr = []
    for i in range(n):
        flag = True
        for r, c in indexes:
            if abs(row-r) == abs(c-i) or i == c:
                flag = False
                break
        if flag:
            arr.append(i)
    for i in arr:
        indexes.append((row, i))
        dfs(indexes, n, row+1, count)
        indexes.pop()
def solution(n):
    poss = []
    answer = [0]
    dfs(poss, n, 0, answer)
    return answer.pop()
```

dfs에서 arr을 True로 초기화 후 False로 바꾸는 것보다 가능한 위치를 배열에 저장하는 방식으로 바꿈으로써,  가능한 위치를 탐색하는 과정과 이후 반복문에서도 시간을 줄여 아슬아슬하게 통과할 수 있었다.
