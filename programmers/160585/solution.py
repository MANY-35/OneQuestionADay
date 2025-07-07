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
    print(o, x)
    print(o_c, x_c)
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


arr = [["OXO", "XOX", "OXO"], 
       ["OOX", "XXO", "OOX"],
       ["XXX", ".OO", "O.."],
    ["OX.", ".O.", ".XO"], 
    ["...", "...", ".O."], 
    ["X.X", "X.O", "O.O"], 
    ["XO.", "OXO", "XOX"], 
    ["OOO", "XOX", "XXO"], 
    ["OOO", "XOX", "X.X"], 
    ["XXX", "OO.", "OO."], 
    [".X.", "...", "..."], 
    [".X.", "X..", ".O."],
    ["XOX", "OXO", "XOX"],
    ["XXX", "XOO", "OOO"],
    ["OOX", "OXO", "XOO"],
    ["OOX", "OXO", "XOX"],
    [".OX", "OXO", "XO."],
    ["OOO", "XX.", "X.."]]

# for i in arr:
#     print(solution(arr))
print(solution(["XXX", "OO.", "OO."]))