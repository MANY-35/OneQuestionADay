# LV2 가장 큰 정사각형 찾기

### 1차 시도 (실패)
```py
def solution(board):
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                i = 1
                while c + i < len(board[r]) and r + i < len(board):
                    if board[r + i][c + i] and board[r+i][c] and board[r][c + i]:
                        area = (i + 1) ** 2
                        if area > answer:
                            answer = area
                    else:
                        break
                    i += 1 
    return answer
```
row및 column의 크기가 1000로 충분히 작아서 O(n^3)으로 풀어도 시간이 충분하다고 판단했다.  
완전 탐색으로 풀었다고 생각했으나, 몇개의 케이스에서 실패했으며 효율성 테스트가 존재했고, 실패했다.

*****

### 2차 시도 (실패)
```py
def solution(board):
    def solution(board):
    answer = 0
    l = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                while c + l < len(board[r]) and r + l < len(board):
                    if board[r + l][c + l] and board[r+l][c] and board[r][c + l]:
                        area = (l + 1) ** 2
                        if area > answer:
                            l += 1
                            answer = area
                    else:
                        break
    return answer
```
최대 길이를 저장하는 방식으로 시간을 줄여보았다.  
효율성 테스트의 시간은 통과하였으나 문제의 답이 틀렸다.  
코드 자체에 문제가 있다는 것을 알아냈다. 연속된 1을 변으로 하는 정사각형을 구해야하는데, 가로 세로의 각 첫줄만 연속된 1을 변으로 하는 것이고 마지막 `board[r+l][c+l]` 에서 마지막에 1이 존재하는지만 판단했기 떄문에 모든 면에 1이 존재하지 않을때도 통과하는 것이 문제였다.  

*****

### 3차 시도 (실패)
```py
def solution(board):
    answer = 0
    for line in board:
        c = 0
        for i in range(len(line)):
            if line[i] == 0:
                c = 0
            else:
                line[i] += c
                c += 1
    l = 0
    for i in range(len(board)):
        for j in range(len(board[i])-1, -1, -1):
            if board[i][j] != 0:
                if i + board[i][j] > len(board) or board[i][j] < l:
                    continue
                for k in range(board[i][j]):
                    flag = True
                    if  board[i+k][j] < board[i][j]:
                        flag = False
                        break
                if flag and answer < board[i][j]**2:
                    answer = board[i][j]**2 
                    l = board[i][j]
    return answer
```
먼저 탐색을 진행하면서 가로로 연속된 1의 갯수들을 카운팅하고 해당 값만큼 세로로 탐색하면서 연속된 1의 갯수가 크다면 사각형인 것으로 판단하고 코드를 작성했으나 3개의 케이스에서 실패했다.  
좀 고민해보니 당장 예제2만 봐도 잘못 판단했다는 것을 알 수 있었다.
*****

### 4차 시도 (성공)
```py
def solution(board): 
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    return max(max(row) for row in board) ** 2
```
DP를 이용하여 각 구역에서 정사각형이 가능한 최대 길이를 저장하는 방식으로 접근하여 풀 수 있다는 사실을 알아냈다.
