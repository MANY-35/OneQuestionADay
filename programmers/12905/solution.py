
def solution(board): 
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    return max(max(row) for row in board) ** 2
    
    

solution([[0,0,1,1],[1,1,1,1]])