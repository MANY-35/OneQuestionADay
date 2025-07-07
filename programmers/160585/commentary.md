# LV2 혼자서 하는 틱택토

### 1차시도 (성공)
```py
def checker(board, ch):
    if board[1][1] == ch:
        if (board[0][0] == ch and board[2][2] == ch) or (board[0][2] == ch and board[2][0] == ch):
            return True
    for i in range(3):
        r, c = 0, 0
        for j in range(3):
            if board[i][j] == ch:
                r += 1
            if board[j][i] == ch:
                c += 1
        if r == 3 or c == 3:
            return True
    return False
def solution(board):
    x, o = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o += 1
            elif board[i][j] == 'X':
                x += 1
    o_c = checker(board, 'O')
    x_c = checker(board, 'X')
    if x > o:
        return 0
    elif x == o:
        if o_c:
            return 0
        return 1
    else:
        if o > x+1:
            return 0
        if x_c:
            return 0
        return 1
```

우선 3X3 보드에서 X의 갯수와 O의 갯수를 카운팅하고 **checker** 함수를 통해 X와 O가 승리조건을 만족했는지 판단한다.  
그 후 x의 갯수와 o의 갯수에 따라 가능한 절차의 게임인지 아닌지 판단하도록 코드를 작성했다.


*****

