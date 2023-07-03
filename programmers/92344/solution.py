board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]


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

print(solution(board, skill))