
def solution(board):
    arr = [[] for _ in range(len(board))]    
    for i in range(len(board)):
        j = 0
        while j < len(board[i]):
            if board[i][j] == 1:
                index = j
                while j < len(board[i]) and board[i][j] == 1:
                    j+=1
                arr[i].append((index, j-index))
            j+=1
    for i in arr:
        print(i)
                
                
    

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])