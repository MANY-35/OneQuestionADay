from collections import deque

def solution(board, moves):
    answer = 0
    stacks = [deque() for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                stacks[j].append(board[i][j])

    
    que = [0]
    for move in moves:
        if len(stacks[move - 1]) == 0:
            continue
        n = stacks[move - 1].popleft()
        if n == que[-1]:
            answer += 2
            que.pop()
        else:
            que.append(n)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])